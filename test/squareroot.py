import numpy as np

def square_root(x):
	""" Calculates the square root of a given number x.

	:Input: The number n (float, >=0).
	:Returns: The square root of the number (float)."""
	if x < 0:
		raise ValueError("The number must be >= 0.")
	root = np.sqrt(x)
	print("The square root of x = {:3.2f} is {:3.3f}.".format(x, root))
	return root

