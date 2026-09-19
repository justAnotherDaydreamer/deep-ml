import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	det_matrix = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
	c = det_matrix

	trace_matrix = matrix[0][0] + matrix[1][1]
	b = - trace_matrix

	# Find roots of quadratic formula
	eigenvalues = [(-b + math.sqrt(b**2 - 4*c))/2, (-b - math.sqrt(b**2 - 4*c))/2]

	# Sort from biggest to lowest
	if eigenvalues[0] < eigenvalues[1]:
		eigenvalues[1], eigenvalues[0] = eigenvalues[0], eigenvalues[1]

	return eigenvalues