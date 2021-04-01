#!/usr/bin/python3
import ADSA_path_finding as apf
	
class MyFinder(apf.draw.Finder):
	"""Integrate into the simple UI	"""
	def __init__(self):
		self.reset()
	
	def step(self, frames):
		self.max_distance = max( 0, self.max_distance + frames )
		self.result = apf.tutorial_1.fill_shortest_path(self.game.board, self.game.start, self.game.end, max_distance = self.max_distance)
		self.set_board(self.result)
		self.set_path(apf.tutorial_1.backtrack_to_start(self.result, self.game.end))
	
	def reset(self):
		self.game = apf.maze.create_wall_maze(20,10)
		self.max_distance = 18
		self.step(0)
	

header_text = """Keys:
	Left - Lower maximum distance
	Right - Increase maximum distance"""
print( header_text )

finder = MyFinder()
finder.run()
