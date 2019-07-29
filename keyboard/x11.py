from os import environ

from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input


class Keyboard:
	class keystates:
		up = X.KeyRelease
		down = X.KeyPress

	def __init__(self, xdisplay=None):
		if not xdisplay:
			xdisplay = Display(environ['DISPLAY'])
		self.__display = xdisplay

	def full_press(self, keycode):
		self.press(keycode, self.keystates.down)
		self.press(keycode, self.keystates.up)

	def press(self, keycode, direction):
		fake_input(self.__display, direction, keycode)
		self.__display.sync()
