# Render the scenes and create the final movie, using a frame sequence approach.
#
# blender -b ap.blend -P scripts/renderScenes.py
#
# The name of the scene should contain, as first char, a number.
# For instance, "1 - First scene".
#
# The scene, used for creating the final output, should not follow that rule.
#
# This is script is useful when the scenes share the same render settings, for
# instance, when the scenes are not full copy.

import bpy

for scene in bpy.data.scenes:
    sceneNumber = scene.name[0]

    if (sceneNumber.isdigit()):
        scene.render.filepath = "//outputs/scene" + sceneNumber + "/"
        scene.render.image_settings.file_format = "PNG"
    else:
        scene.render.filepath = "//outputs/ap.mpg"
        scene.render.image_settings.file_format = "FFMPEG"

    print("RENDERING SCENE: %s" % scene.render.filepath)
    bpy.ops.render.render(animation=True, scene=scene.name)
