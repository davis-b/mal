from math import modf
from time import sleep


class BaseCursor:
	class buttons:
		left = 1
		middle = 2
		right = 3
		mousewheel_up = 4
		mousehweel_down = 5
		mousewheel_left = 6
		mousewheel_right = 7

	def __init__(self):
		pass

	def btn_down(self, button):
		raise NotImplementedError
	
	def btn_up(self, button):
		raise NotImplementedError

	@property
	def pos(self):
		raise NotImplementedError

	def move_to(self, x, y):
		raise NotImplementedError

	def move_by(self, x, y):
		start_x, start_y = self.pos
		self.move_to(start_x + x, start_y + y)

	def click(self, button, xy=None):
		if xy:
			self.move_to(*xy)
		self.btn_down(button)
		self.btn_up(button)
		
	def drag(self, x, y, drag_time=0, click=True):
		x2, y2 = self.pos

		if click:
			self.btn_down(self.buttons.left)
		
		abs_max_x_y = abs(max(x,y))
		drag_time /= abs_max_x_y
		
		x_direction = -1 if x < 0 else 1
		y_direction = -1 if y < 0 else 1
		x2_trajectory = x_direction
		y2_trajectory = y_direction
		if x > y:
			y2_trajectory = (abs(y) / abs(x)) * y_direction
		elif x != y:
			x2_trajectory = (abs(x) / abs(y)) * x_direction
			
		x2_frac, x2_whole = modf(x2_trajectory)
		y2_frac, y2_whole = modf(y2_trajectory)
		x2_frac = abs(x2_frac); y2_frac = abs(y2_frac)
		x2_whole = int(x2_whole); y2_whole = int(y2_whole)
		x_leftover = 0.0
		y_leftover = 0.0
		for i in range(abs_max_x_y):
			x2 += x2_whole
			y2 += y2_whole
			x_leftover += x2_frac
			y_leftover += y2_frac
			if x_leftover > 1:
				x2 += 1 * x_direction
				x_leftover -= 1
			if y_leftover > 1:
				y2 += 1 * y_direction
				y_leftover -= 1
			self.move_to(x2, y2)
			sleep(drag_time)	

		if click:
			self.btn_up(self.buttons.left)

	def clicks(self, button, amount, time_between_clicks):
		for i in range(amount):
			self.click(button)
			sleep(time_between_clicks / amount)

	def print_current_pos(self, delay):
		from sys import stdout
		old_g = ''
		print('')
		try:
			while True:
				x, y = self.pos
				g = str(x) + ', ' + str(y) + ' '
				if g != old_g:
					stdout.write(g)
					stdout.write('\b' * len(g))
					stdout.flush()
				old_g = g
				sleep(delay)
		except KeyboardInterrupt:
			print('')
