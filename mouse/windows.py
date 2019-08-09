import ctypes
from time import sleep

from .base import BaseCursor


u32 = ctypes.windll.user32

class Cursor_POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong),
                ("y", ctypes.c_ulong)]
				
mousewheel_delta = 120
windows_keycodes = {
	'left': 2,
	'middle': 32,
	'right': 8,
	'mousewheel_vertical': 0x800,
	'mousewheel_horizontal': 0x1000,
}

class Cursor(BaseCursor):

	def __init__(self):
		self._keycode_transformations = {
			self.buttons.left: windows_keycodes['left'],
			self.buttons.middle: windows_keycodes['middle'],
			self.buttons.right: windows_keycodes['right'],
			self.buttons.mousewheel_up: windows_keycodes['mousewheel_vertical'],
			self.buttons.mousewheel_down: windows_keycodes['mousewheel_vertical'],
			self.buttons.mousewheel_left: windows_keycodes['mousewheel_horizontal'],
			self.buttons.mousewheel_right: windows_keycodes['mousewheel_horizontal'],
		}

	def btn_down(self, button):
		windows_keycode = windows_keycodes[button]
		if windows_keycode == windows_keycodes['mousewheel_horizontal']:
			direction = 1 if button == self.buttons.mousewheel_right else -1
			self._btn(windows_keycode, dwData=direction * mousewheel_delta)
		if windows_keycode == windows_keycodes['mousewheel_vertical']:
			direction = 1 if button == self.buttons.mousewheel_up else -1
			self._btn(windows_keycode, dwData=direction * mousewheel_delta)
		else:
			self._btn(windows_keycode)
	
	def btn_up(self, button):
		windows_keycode = windows_keycodes[button]
		if windows_keycode == windows_keycodes['mousewheel_horizontal'] or windows_keycode == windows_keycodes['mousewheel_vertical']:
			return
		else:
			self._btn(windows_keycode * 2)
	
	def _btn(self, windows_keycode, dwData=0):
		# NOTE Function has been superseded by SendInput
		u32.mouse_event(windows_keycode, 0, 0, dwData, 0)
	
	@property
	def pos(self):
		"""Returns current cursor position. Accepts no arguments.  """
		cursor = Cursor_POINT()
		u32.GetCursorPos(ctypes.byref(cursor))
		return (int(cursor.x), int(cursor.y))
	
	def move_to(self, x, y):
		u32.SetCursorPos(x, y)