#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

""" Example showing use of FixedString. ESC to quit

FixedString should be faster for rendering large quantities of text as
it only requires two triangles for the whole text rather than two triangles
for each letter"""
import demo
import pi3d

DISPLAY = pi3d.Display.create()
DISPLAY.set_background(0.9, 0.9, 0.9, 0)
flatsh = pi3d.Shader("uv_flat")
shader = pi3d.Shader("uv_bump")
CAMERA = pi3d.Camera()
CAMERA2D = pi3d.Camera(is_3d=False)
pi3d.Light(lightpos=(10, -10, 2))
mytext = '''Pi3D is a Python module that
aims to greatly simplify
writing 3D in Python whilst
giving access to the power
of the Raspberry Pi GPU.
'''

f1 = pi3d.Font('fonts/NotoSans-Regular.ttf', font_size=32, background_color=(200,140,20,128))
f2 = pi3d.Font('fonts/NotoSans-Regular.ttf', font_size=32, background_color=(200,140,20,128), shadow_radius=2, shadow=(255,0,0,255))
f3 = pi3d.Font('fonts/NotoSans-Regular.ttf', font_size=32)
f4 = pi3d.Font('fonts/NotoSans-Regular.ttf', font_size=32, shadow_radius=1, shadow=(255,0,0,255))
f5 = pi3d.Font('fonts/NotoSans-Regular.ttf', font_size=45, shadow_radius=2, shadow=(0,0,0,255))

strs = [
    pi3d.String(font=f1, string=mytext, camera=CAMERA2D, is_3d=False, x=-300, y=-200, z=0),
    pi3d.String(font=f2, string=mytext, camera=CAMERA2D, is_3d=False, x=-300, y=200, z=1),
    pi3d.String(font=f3, string=mytext, camera=CAMERA2D, is_3d=False, x=300, y=-200, z=2),
    pi3d.String(font=f4, string=mytext, camera=CAMERA2D, is_3d=False, x=300, y=200, z=3),
    pi3d.String(font=f5, string=mytext, camera=CAMERA2D, is_3d=False)]
for s in strs:
  s.set_shader(flatsh)
    
mykeys = pi3d.Keyboard()
while DISPLAY.loop_running():
  for s in strs:
    s.draw()
  if mykeys.read() == 27:
    mykeys.close()
    DISPLAY.destroy()
    break
