import porespy as ps
import numpy as np
from skimage import measure
from collections import namedtuple
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh


#SIZE = 10
#SHAPE = list(SIZE for _ in range(3))


def padding_structure(structure):
    return np.pad(structure, pad_width=1, mode='constant', constant_values=False)


def generate_blobs(SHAPE, porosity, blobiness):
    blobs = ps.generators.blobs(
        shape=SHAPE, porosity=porosity, blobiness=blobiness)
    maze = blobs
    blobs = np.logical_not(blobs)

    #blobs = ps.filters.trim_floating_solid(blobs)
    #blobs = ps.filters.fill_blind_pores(blobs)
    return padding_structure(blobs), maze


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
    mesh_fig = mplot3d.art3d.Poly3DCollection(
        mesh_object.verts[mesh_object.faces])
    mesh_fig.set_edgecolor('k')
    axes.add_collection3d(mesh_fig)
    scale = mesh_object.verts.flatten('F')
    axes.auto_scale_xyz(scale, scale, scale)
    axes.set_title(title)


def save_mesh_to_stl(mesh_object, filename):
    mesh_object = list(map(lambda x: (0, x.tolist(), 0),
                           mesh_object.verts[mesh_object.faces]))
    mesh_object = np.array(mesh_object, dtype=mesh.Mesh.dtype)
    mesh_object = mesh.Mesh(mesh_object, remove_empty_areas=True)
    mesh_object.save(filename)


def structure_processing(voxels_structure, title):
    mesh_object = mesh_from_voxels(voxels_structure)
    #show_mesh_figure(mesh_object, title)
    save_mesh_to_stl(mesh_object, f'{ title }.stl')


#structure_processing(generate_blobs(), 'blobs')
# lt.show()
