# mal - Minimal Automation Library #

_mal_ aids in GUI automation by emulating/injecting keyboard and mouse input.

## Overview ##

#### Keyboard ####
The `Keyboard` class has two methods.  
`press` takes a keycode and a direction (accessed via Keyboard.keystates.[up or down]).  
`full_press` takes a keycode and simply calls `press` with down and then up.

#### Cursor ####
The `Cursor` class can click buttons and move the cursor relatively and to exact coordinates.  
A list of cursor methods:
* click (button, xy)
* move_to (x, y)
* move_by (x, y)
* drag (x, y, time: int, click: bool)
* pos \[@property]  

When calling `click`, you will need to provide an integer representing a button.  
The following button values can be found in the Cursor.buttons container: left, middle, right, mousewheel_\[up|down|left|right]

---


## Requirements ##

_mal_ works on both Windows and Linux systems.  

Beyond python, there are no requirements for Windows.  
Linux requires X11 and the [python xlib](https://github.com/python-xlib/python-xlib) library.  

---


## Drawbacks ##

Due to the method used to emulate input on Windows, _mal_ cannot interact with many things requiring administrative privileges, including UAC prompts.

---


### To-Do ###
In the future, perhaps this library could be extended to include the following:
* Lower level input injection. If _mal_ could emulate hardware input, that would be optimal.
* Remove X11 dependency. This plays into the previous to-do, but it is worth mentioning on its own.
* Include other automation aspects, such as: switching the active window, enumerating all windows, sending keypresses to windows which are not focused.