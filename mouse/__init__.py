from sys import platform
if platform == 'linux':
	from .x11 import Cursor
elif platform == 'win32':
	from .windows import Cursor
else:
	raise NotImplementedError(platform, 'OS not supported')