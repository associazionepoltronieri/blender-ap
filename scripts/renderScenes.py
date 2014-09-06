# Render the scenes and create the final movie.
# The scene are ordered: the final one is to compose the final output.

for scene in bpy.data.scenes:
    print("RENDERING SCENE: %s" % scene.name)
    bpy.ops.render.render(animation=True, scene=scene.name)
