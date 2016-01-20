#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

""" Example showing what can be left out. ESC to quit"""
import demo
import pi3d
from pi3d.constants import GL_LINEAR, GL_NEAREST
DISPLAY = pi3d.Display.create()
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
sprite = pi3d.ImageSprite(pi3d.Texture("textures/icon1.png", mipmap=False, filter=GL_NEAREST), shader,
                          w=150.0, h=150.0, x=-200, y=200, z=5.0)
sprite2 = pi3d.ImageSprite(pi3d.Texture("textures/icon1.png", mipmap=False, filter=GL_LINEAR), shader,
                           w=150.0, h=150.0, x=200, y=200, z=6.0)
sprite3 = pi3d.ImageSprite(pi3d.Texture("textures/icon1.png", mipmap=True, filter=GL_NEAREST), shader,
                           w=150.0, h=150.0, x=-200, y=-200, z=7.0)
sprite4 = pi3d.ImageSprite(pi3d.Texture("textures/icon1.png", mipmap=True, filter=GL_LINEAR), shader,
                           w=150.0, h=150.0, x=200, y=-200, z=8.0)
sprites=[sprite, sprite2, sprite3, sprite4]
pos=[(-75, 75, 5), (75, 75, 6), (-75, -75, 7), (75, -75, 8)]
mykeys = pi3d.Keyboard()
scale = 1.
ds = 1.005
while DISPLAY.loop_running():
  for i, s in enumerate(sprites):
    s.draw()
    s.scale(scale, scale, scale)
    s.position(pos[i][0]*scale, pos[i][1]*scale, pos[i][2])
    #s.rotateIncZ(1)

  if ds < 0:
     scale /=abs(ds)
  if ds > 0:
     scale *= ds

  if scale > 3.0:
    ds = -ds
  if scale < 0.3:
    ds = -ds

  if mykeys.read() == 27:
    mykeys.close()
    DISPLAY.destroy()
    break
