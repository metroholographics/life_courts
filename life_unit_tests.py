from life_courts import next_board_state

NUM_TESTS = 3

def check_dead_0_alive():
	# cell with 0 live neighbours stay dead
	init_state = [ 
		[0,0,0],
		[0,0,0],
		[0,0,0],
	]
	exp_state = [ 
		[0,0,0],
		[0,0,0],
		[0,0,0],
	]

	actual_next = next_board_state(init_state)

	if actual_next == exp_state:
		print("Passed check_dead_0_alive...")
		return True
	print("Failed check_dead_0_alive")
	print(f"Expected: {exp_state}")
	print(f"Actual: {actual_next}")
	return False

def check_alive_2_3_alive():
	# cell with 0 live neighbours stay dead
	init_state = [ 
		[0,1,0],
		[0,1,0],
		[1,0,0],
	]
	exp_state = [ 
		[0,0,0],
		[1,1,0],
		[0,0,0],
	]

	actual_next = next_board_state(init_state)

	if actual_next == exp_state:
		print("Passed check_alive_2_3_alive...")
		return True
	print("Failed check_alive_2_3_alive")
	print(f"Expected: {exp_state}")
	print(f"Actual: {actual_next}")
	return False

def check_alive_4_alive():
	# cell with 0 live neighbours stay dead
	init_state = [ 
		[0,1,0],
		[1,1,1],
		[0,1,0],
	]
	exp_state = [ 
		[1,1,1],
		[1,0,1],
		[1,1,1],
	]

	actual_next = next_board_state(init_state)

	if actual_next == exp_state:
		print("Passed check_alive_4_alive...")
		return True
	print("Failed check_alive_4_alive")
	print(f"Expected: {exp_state}")
	print(f"Actual: {actual_next}")
	return False

if __name__ == "__main__":
	pass_count = 0
	if check_dead_0_alive():
		pass_count += 1
	if check_alive_2_3_alive():
		pass_count += 1
	if check_alive_4_alive():
		pass_count += 1

	print(f"Passed {pass_count}/{NUM_TESTS} tests")

