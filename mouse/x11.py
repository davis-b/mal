from os import environ
from time import sleep

from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

from .base import BaseCursor


class Cursor(BaseCursor):
	class buttons:
		left = 1
		middle = 2
		right = 3
	
	def __init__(self, display=None):
		if not display:
			display = Display(environ['DISPLAY'])
		self.display = display

	@property
	def pos(self):
		data = self.display.screen().root.query_pointer()._data
		return data['root_x'], data['root_y']

	def move_to(self, x, y):
		# self.display.screen().root.warp_pointer(x, y)
		fake_input(self.display, X.MotionNotify, x=x, y=y)
		self.display.flush()
	
	def btn_down(self, button):
		fake_input(self.display, X.ButtonPress, button)
		# Should we be using sync instead of flush?
		self.display.flush()

	def btn_up(self, button):
		fake_input(self.display, X.ButtonRelease, button)
		self.display.flush()