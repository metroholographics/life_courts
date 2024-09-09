import random

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
			if random_num >= 0.5:
				state[list][cell] = 0
			else:
				state[list][cell] = 1
	return state

def render(state):

	for list in range(len(state)):
		for cell in state[list]:
			if cell == 0:
				char = " "
			else:
				char = "~"
			print(f"{char:^3} ", end = "")
		print()


if __name__ == "__main__":
	w = 5
	h = 5
	game_state = random_state(20,20)
	render(game_state)
