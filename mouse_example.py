from mouse import Cursor

if __name__ == '__main__':
	cursor = Cursor()
	cursor.click(cursor.buttons.left)
	print(cursor.pos)
	cursor.drag(x=10, y=200, drag_time=1, click=False)
	print(cursor.pos)
	cursor.move_to(1000, 1000)