import random
import time
import os

CHANCE_DEAD = 0.2
TOAD = "./toad.txt"
GGG = "./GGG.txt"

HOT_EMOJI = '\U0001F975'
DEVIL_EMOJI = '\U0001F608'
TREE_EMOJI = '\U0001F332'
CHIPMUNK_EMOJI = '\U0001F43F'
CUNEIFORM = '\U00012031'

def dead_state(height, width):
	state = []
	for y in range(height):
		line_state = []
		for x in range(width):
			line_state.append(0)
		state.append(line_state)
	return state

def random_state(height, width):
	state = dead_state(height, width)

	for list in range(height):
		for cell in range(width):
			random_num = random.random()
			if random_num >= CHANCE_DEAD:
				state[list][cell] = 0
			else:
				state[list][cell] = 1
	return state

def render(state, alive = '#\U00002591', dead = '_|'):
	alive = alive
	dead = dead
	for list in range(len(state)):
		for cell in state[list]:
			if cell == 0:
				char = dead
			else:
				char = alive
			print(f"{char:^2} ", end = "")
		print()

def next_board_state(state):
	h = len(state)
	w = len(state[0])
	next_state = dead_state(h, w)

	for list in range(h):
		for i in range(w):
			check_matrix = gen_check_matrix(state, list, i)
			alive_neighbours = count_alive(check_matrix)
			#check_matrix[1][1] is current cell
			if check_matrix[1][1] == 'A':
				if alive_neighbours <= 1:
					next_state[list][i] = 0
				elif alive_neighbours <= 3:
					next_state[list][i] = 1
				elif alive_neighbours > 3:
					next_state[list][i] = 0
			elif check_matrix[1][1] == 'D':
				if alive_neighbours == 3:
					next_state[list][i] = 1
			# print(check_matrix)
	return next_state

def gen_check_matrix(state, list_idx, i):
	check_matrix = dead_state(3,3)

	if state[list_idx][i] == 0:
		check_matrix[1][1] = "D"
	else:
		check_matrix[1][1] = "A"

	#top row:
	if list_idx - 1 >= 0:
		#top left
		if i - 1 >= 0:
			check_matrix[0][0] = state[list_idx-1][i-1]
		#top middle:
		check_matrix[0][1] = state[list_idx-1][i]
		#top right
		if i + 1 < len(state[0]):
			check_matrix[0][2] = state[list_idx-1][i+1]
	#mid-left
	if i - 1 >= 0:
		check_matrix[1][0] = state[list_idx][i-1]
	#mid-right
	if i + 1 < len(state[0]):
		check_matrix[1][2] = state[list_idx][i+1]
	#bottom row
	if list_idx + 1 < (len(state)):
		#bottom left
		if i - 1 >= 0:
			check_matrix[2][0] = state[list_idx+1][i-1]
		#bottom middle
		check_matrix[2][1] = state[list_idx+1][i]
		#bottom right:
		if i + 1 < len(state[0]):
			check_matrix[2][2] = state[list_idx+1][i+1]

	return check_matrix

def count_alive(check_m):
	num_alive = 0
	for list in range(len(check_m)):
		for i in range(len(check_m[0])):
			if check_m[list][i] == 1:
				num_alive += 1
	return num_alive

def load_board_state(filepath, h = 10, w = 10):
	if filepath == "random":
		return random_state(h, w)

	state = []
	with open(filepath, "r") as f:
		for line in f:
			line_s = []
			for s in line:
				if s != '\n':
					s = int(s)
					line_s.append(s)
			state.append(line_s)
	return state

if __name__ == "__main__":

	# enter ("random", h, w) for random
	game_state = load_board_state(GGG)

	while True:
		os.system('clear')
		render(game_state)
		game_state = next_board_state(game_state)
		time.sleep(0.075)



