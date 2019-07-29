import ctypes
from time import sleep

from .base import BaseCursor


u32 = ctypes.windll.user32

class Cursor_POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong),
                ("y", ctypes.c_ulong)]
				
class Cursor(BaseCursor):
	class buttons:
		left = 2
		middle = 32
		right = 8

	def __init__(self):
		pass

	def btn_down(self, button):
		# NOTE Function has been superseded by SendInput
		u32.mouse_event(button, 0, 0, 0, 0)
	
	def btn_up(self):
		# NOTE Function has been superseded by SendInput
		u32.mouse_event(button * 2, 0, 0, 0, 0)
	
	@property
	def pos(self):
		"""Returns current cursor position. Accepts no arguments.  """
		cursor = Cursor_POINT()
		u32.GetCursorPos(ctypes.byref(cursor))
		return (int(cursor.x), int(cursor.y))
	
	def move_to(self, x, y):
		u32.SetCursorPos(x, y)