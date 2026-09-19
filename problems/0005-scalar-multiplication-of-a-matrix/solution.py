def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	
	# Just go through the elements and multiply them
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] *= scalar
	
	return matrix