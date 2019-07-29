import ctypes
u32 = ctypes.windll.user32


class Keyboard:
	class keystates:
		up = 0x02
		down = 0

	def __init__(self):
		pass

	def full_press(self, keycode):
		self.press(keycode, self.keystates.down)
		self.press(keycode, self.keystates.up)

	def press(self, keycode, direction):
		return ctypes.windll.user32.keybd_event(keycode, 0, direction, 0)

