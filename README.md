Cartoon to promote Associazione Poltronieri
===========================================

The Association logo becomes a storm of butterflies. They travel on the fields,
to the city, they take care the children going to the school, they sponsor the
projects of the Association and, at last, they come back to rest in the
Association logo.

Furthemore the short tale is told from the point of view of a child.

Technical details
=================

The cartoon is implemented using [Blender](http://www.blender.org/).

The rendering tecnique is called [Non-Photorealistic Rendering](http://wiki.blender.org/index.php/Dev:Ref/Release_Notes/2.71/Freestyle). The rendering settings are stolen from the
Teapot example contained in that link.

There are five scenes and one more to assembly all the scenes and the music in
the Video Sequence Editor (VSE). The animation is rendered using the [frame sequence approach](http://wiki.blender.org/index.php/Doc:2.6/Manual/Render/Animations).

To render all the scenes and to get the movie in `outputs` folder, you need to
execute the following snippet (`scripts/renderScenes.py`):

```
for scene in bpy.data.scenes:
    print("RENDERING SCENE: %s" % scene.name)
    bpy.ops.render.render(animation=True, scene=scene.name)
```

Credit
======

- Music: Romaria, Elis Regina.
