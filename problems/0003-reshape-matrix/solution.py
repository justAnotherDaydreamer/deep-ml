import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	
	# Turn a to numpy array
	a = np.array(a)

	# Check for can't be returned
	if new_shape[0]*new_shape[1] != a.shape[0]*a.shape[1]:
		return []

	reshaped_matrix = a.reshape(new_shape[0], new_shape[1])
	return reshaped_matrix