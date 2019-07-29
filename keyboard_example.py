from keyboard import Keyboard
from keynames import keycode_names

if __name__ == '__main__':
	kb = Keyboard()
	w = keycode_names.get('l', 0)
	shift = keycode_names['win']
	kb.press(shift, kb.keystates.down)
	kb.press(w, kb.keystates.down)
	kb.press(w, kb.keystates.up)
	kb.press(shift, kb.keystates.up)