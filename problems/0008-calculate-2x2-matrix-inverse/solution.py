def determinant(X: list[list[int|float]]):
	result = X[0][0]*X[1][1] - X[0][1]*X[1][0]
	return result

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
	# If det = 0
	if determinant(matrix) == 0:
		return None

	# Else
	deter = 1/determinant(matrix)
	inverted = [[deter * matrix[1][1], -deter * matrix[0][1]], [-deter * matrix[1][0], deter * matrix[0][0]]]
	return inverted