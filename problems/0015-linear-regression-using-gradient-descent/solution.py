import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent

    # Iterate acording to the amount given by input
    while iterations > 0:
        # Keep a verson of theta so we can use it without being modified yet within an inner loop
        theta_kept = np.array(theta)
        # For each iteration, find the new theta vector
        for i in range(n):
            # h is the column vector that contains the prediction every observation or row of X,
            # using the current theta
            h = X @ theta_kept
            # The better value for each row of theta vector is found by
            # subtracting it with [alpha * (1/m) * (partial derivative of the loss funciton)], 
            # which reduces to the following, where
            # y is the column vector for the labels, and X[:,i] calls all observations for the x_i feature
            theta[i] -= alpha * (1/m) * [(h - y).T @ X[:,i]][0]  # [0] so the list becomes a float

        iterations -=1

    return theta.flatten()