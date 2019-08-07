from time import sleep
from mouse import Cursor

if __name__ == '__main__':
	cursor = Cursor()
	cursor.click(cursor.buttons.left)
	cursor.click(cursor.buttons.mousewheel_down)
	start_pos = cursor.pos
	print(start_pos)
	cursor.drag(x=10, y=200, drag_time=1, click=False)
	print(cursor.pos)
	cursor.move_to(*start_pos)
	sleep(0.4)
	cursor.move_by(0, 100)
	print(cursor.pos)