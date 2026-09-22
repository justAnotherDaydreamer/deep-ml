import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	# Recall that the normal equation for each coef of linear regression are:
	# => [((X^T)X)^-1](X^T)y
	X = np.array(X)
	y = np.array(y)

	trans_X = X.transpose()
	theta = (trans_X @ X)  # Inner product
	theta = np.linalg.inv(theta) # Inverse it
	theta = (theta @ trans_X @ y)  # Inner product

	theta = np.round(theta, 4)  # Round to 4 decimal points

	return theta