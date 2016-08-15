#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

""" Example showing what can be left out. ESC to quit"""
import demo
import pi3d
import sys
import bg
import argparse

import ctypes
from pi3d.util.Ctypes import c_ints
import numpy as np
from PIL import Image

from pi3d.constants import *
from pi3d.util import Log

from pi3d.Display import Display

parser = argparse.ArgumentParser(description='Test dispmanx alpha blending')
parser.add_argument('--dispmanx', dest='dispmanx_bg', action='store_true',
                   help='draw bg with dispmanx instead of opengl')
parser.add_argument('--premult', dest='premult', action='store_true',
                   help='use DISPMANX_FLAGS_ALPHA_PREMULT on the opengl dispmanx element')


args = parser.parse_args()

def screenshot(filestring):
  w, h = Display.INSTANCE.width, Display.INSTANCE.height
  img = np.zeros((h, w, 4), dtype=np.uint8)
  opengles.glReadPixels(0, 0, w, h, GL_RGBA, GL_UNSIGNED_BYTE, img.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)))
  img = img[::-1,:,:4].copy()
  if filestring is None:
    return img

  im = Image.frombuffer('RGBA', (w, h), img, 'raw', 'RGBA', 0, 1)
  im.save(filestring, quality=90)


def patched_create_surface(self, x=0, y=0, w=0, h=0, layer=0):
  print("Creating a patched surface")
  #Set the viewport position and size
  dst_rect = c_ints((x, y, w, h))
  src_rect = c_ints((x, y, w << 16, h << 16))

  if PLATFORM == PLATFORM_PI:
    self.dispman_display = bcm.vc_dispmanx_display_open(0) #LCD setting
    self.dispman_update = bcm.vc_dispmanx_update_start(0)
    alpha = ctypes.byref(c_ints((1<<16, 0, 0)))
    print("Using premult flag")

    self.dispman_element = bcm.vc_dispmanx_element_add(
      self.dispman_update,
      self.dispman_display,
      layer, ctypes.byref(dst_rect),
      0, ctypes.byref(src_rect),
      DISPMANX_PROTECTION_NONE,
      alpha, 0, 0)

    nativewindow = c_ints((self.dispman_element, w, h + 1))
    bcm.vc_dispmanx_update_submit_sync(self.dispman_update)

    nw_p = ctypes.pointer(nativewindow)
    self.nw_p = nw_p

    self.surface = openegl.eglCreateWindowSurface(self.display, self.config, self.nw_p, 0)
  else:
    print("Error - this is supposed to run on the PI")

  assert self.surface != EGL_NO_SURFACE
  r = openegl.eglMakeCurrent(self.display, self.surface, self.surface,
                             self.context)
  assert r

  #Create viewport
  opengles.glViewport(0, 0, w, h)



bgfile = "textures/cc1.jpg"

bgcolor = (0.0, 0.0, 0.0, 0.0)

if args.premult: 
  pi3d.util.DisplayOpenGL.DisplayOpenGL.create_surface = patched_create_surface

DISPLAY = pi3d.Display.create(background=bgcolor, layer=1)
DISPLAY.frames_per_second = 10
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)

if args.dispmanx_bg:
    print("Background using Dispmanx")
    dxbg = bg.UpdatingBGDisplay(960, 540, -10)
    dxbg.setImg(bgfile)
else:
    print("Drawing background in OpenGL")

bg = pi3d.ImageSprite(bgfile, shader, w=DISPLAY.width, h=DISPLAY.height, z=10)
t = pi3d.Texture("textures/upload.png")
sprite = pi3d.ImageSprite(t, shader, w=512, h=512, x=-300, z=5)
sprite.set_alpha(0.2)
sprite2 = pi3d.ImageSprite(t, shader, w=512, h=512, x=300, z=5)
sprite2.set_alpha(0.8)

doscr = True
while DISPLAY.loop_running():
  if not args.dispmanx_bg:
    bg.draw()
    
  sprite.draw()
  sprite2.draw()

  if doscr:
      screenshot("scr_{}_{}.png".format('dispmanx' if args.dispmanx_bg else 'gl',
                                        'premult' if args.premult else '0'))
      doscr = False
