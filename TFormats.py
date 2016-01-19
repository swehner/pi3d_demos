#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

""" Example showing what can be left out. ESC to quit"""
import demo
import pi3d
DISPLAY = pi3d.Display.create(x=150, y=150)
shader = pi3d.Shader("uv_flat")
shader2 = pi3d.Shader("uv_flat_color")
CAMERA = pi3d.Camera(is_3d=False)
sprite = pi3d.ImageSprite("textures/lenna_l.png", shader, w=150.0, h=150.0, z=5.0)
sprite2 = pi3d.ImageSprite("textures/lenna_rgb.png", shader, w=150.0, h=150.0, z=5.0)
sprite3 = pi3d.ImageSprite(pi3d.Texture("textures/lenna_l.png", i_format=pi3d.constants.GL_ALPHA), shader2, w=150.0, h=150.0, z=5.0)
sprite4 = pi3d.ImageSprite("textures/lenna_rgba.png", shader, w=150.0, h=150.0, z=5.0)
sprite5 = pi3d.ImageSprite("textures/lenna_la.png", shader, w=150.0, h=150.0, z=5.0)
sprites=[sprite, sprite2, sprite3, sprite4, sprite5]
mykeys = pi3d.Keyboard()
xloc = 100.0
dx = 2.1
yloc = 100.0
dy = 1.13
color=0
colors=[(1, 0, 0), (0, 1, 0), (0, 0, 1), (0.5, 0.5, 0), (0, 0.5, 0.5)]
while DISPLAY.loop_running():
  for s in sprites:
    s.draw()
    #s.rotateIncZ(1)

  sprite.position(xloc, yloc, 9)
  sprite2.position(-xloc, -yloc, 8)
  sprite3.position(xloc, -yloc, 7)
  sprite4.position(-xloc, yloc, 6)
  sprite5.position(xloc*0.5, yloc*0.5, 5)
  sprite3.set_material(colors[color%len(colors)])
  if xloc > 300.0:
    dx = -2.1
    color+=1
  elif xloc < -300.0:
    dx = 2.1
    color+=1
  if yloc > 300.0:
    dy = -1.13
  elif yloc < -300.0:
    dy = 1.13
  xloc += dx
  yloc += dy

  if mykeys.read() == 27:
    mykeys.close()
    DISPLAY.destroy()
    break
