import porespy as ps
import numpy as np
from scipy import stats
from skimage import measure
from collections import namedtuple
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh


SIZE = 50
SHAPE = list(SIZE for _ in range(3))


def padding_structure(structure):
    return np.pad(structure, pad_width=1, mode='constant', constant_values=False)


def generate_blobs():
    blobs = ps.generators.blobs(shape=SHAPE, porosity=0.5, blobiness=1)
    blobs = ps.filters.trim_floating_solid(blobs)
    blobs = ps.filters.fill_blind_pores(blobs)
    return padding_structure(blobs)


def generate_bundle_of_tubes():
    bundle_of_tubes = ps.generators.bundle_of_tubes(shape=SHAPE, spacing=10)
    return padding_structure(bundle_of_tubes)


def generate_cylinders():
    cylinders = ps.generators.cylinders(shape=SHAPE, radius=SIZE//25, ncylinders=50, phi_max=10, theta_max=10)
    return padding_structure(cylinders)


def generate_lattice_spheres():
    lattice_spheres = ps.generators.lattice_spheres(shape=SHAPE, radius=SIZE//5, lattice='bcc')
    return lattice_spheres


def generate_polydisperse_spheres():
    polydisperse_spheres = ps.generators.polydisperse_spheres(
        shape=SHAPE, porosity=0.5, dist=stats.norm(loc=SIZE//5, scale=SIZE//10)
    )
    return padding_structure(polydisperse_spheres)


def mesh_from_voxels(structure):
    verts, faces, norm, val = measure.marching_cubes_lewiner(structure)
    result = namedtuple('mesh', ('verts', 'faces', 'norm', 'val'))
    result.verts = verts  # - 1/2
    result.faces = faces
    result.norm = norm
    result.val = val
    return result


def show_mesh_figure(mesh_object, title):
    fig = plt.figure()
    axes = mplot3d.Axes3D(fig)
    mesh_fig = mplot3d.art3d.Poly3DCollection(mesh_object.verts[mesh_object.faces])
    mesh_fig.set_edgecolor('k')
    axes.add_collection3d(mesh_fig)
    scale = mesh_object.verts.flatten('F')
    axes.auto_scale_xyz(scale, scale, scale)
    axes.set_title(title)


def save_mesh_to_stl(mesh_object, filename):
    mesh_object = list(map(lambda x: (0, x.tolist(), 0), mesh_object.verts[mesh_object.faces]))
    mesh_object = np.array(mesh_object, dtype=mesh.Mesh.dtype)
    mesh_object = mesh.Mesh(mesh_object, remove_empty_areas=True)
    mesh_object.save(filename)


def structure_processing(voxels_structure, title):
    mesh_object = mesh_from_voxels(voxels_structure)
    show_mesh_figure(mesh_object, title)
    save_mesh_to_stl(mesh_object, f'{ title }.stl')


def main():
    structure_processing(generate_blobs(), 'blobs')
    structure_processing(generate_bundle_of_tubes(), 'bundle_of_tubes')
    structure_processing(generate_cylinders(), 'cylinders')
    structure_processing(generate_lattice_spheres(), 'lattice_spheres')
    structure_processing(generate_polydisperse_spheres(), 'polydisperse_spheres')
    plt.show()


if __name__ == '__main__':
    main()