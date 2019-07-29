from sys import platform
if platform == 'linux':
	from .x11 import Keyboard
elif platform == 'win32':
	from .windows import Keyboard