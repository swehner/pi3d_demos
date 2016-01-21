#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

""" Example showing what can be left out. ESC to quit"""
import demo
import pi3d
from pi3d.constants import GL_ALPHA, GL_LUMINANCE, GL_LUMINANCE_ALPHA, GL_RGB, GL_RGBA
DISPLAY = pi3d.Display.create(x=0,y=0,w=300,h=200)
shader = pi3d.Shader("uv_flat")
shader2 = pi3d.Shader("uv_flat_color")
CAMERA = pi3d.Camera(is_3d=False)

gl_formats = [None, GL_ALPHA, GL_LUMINANCE, GL_LUMINANCE_ALPHA, GL_RGB, GL_RGBA]
files = ['lenna_l.png', 'lenna_la.png', 'lenna_rgb.png', 'lenna_rgba.png']
startx = -125
posy = 75
dx = 50
dy = -50
w = 50
h = 50
sprites = []
for f in files:
  posx = startx
  for gf in gl_formats:
    shad = shader2 if gf == GL_ALPHA else shader
    s = pi3d.ImageSprite(pi3d.Texture('textures/' + f, i_format=gf), shad, w=w, h=h, z=5.0, x=posx, y=posy)
    s.set_material((1,0,0))
    posx += dx
    sprites.append(s)

  posy +=dy
 
mykeys = pi3d.Keyboard()
while DISPLAY.loop_running():
  for s in sprites:
    s.draw()

  if mykeys.read() == 27:
    mykeys.close()
    DISPLAY.destroy()
    break
