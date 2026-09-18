def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means = []

	# Let the matrix be A_ij
	if mode == "column":
		for j in range(len(matrix[0])):
			# Create variable for the sum of each column:
			sum_per_column = 0
			for i in range(len(matrix)):
				sum_per_column += matrix[i][j]
			# Divide sum by amount of rows in a column: 
			mean = sum_per_column / len(matrix)

			means.append(mean)
	
	else:
		for i in range(len(matrix)):
			# Create variable for the sum of each column:
			sum_per_row = 0
			for j in range(len(matrix[0])):
				sum_per_row += matrix[i][j]
			# Divide sum by amount of rows in a column: 
			mean = sum_per_row / len(matrix[0])

			means.append(mean)

	return means