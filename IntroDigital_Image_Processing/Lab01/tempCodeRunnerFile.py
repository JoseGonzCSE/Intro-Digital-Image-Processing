# Create two-dimensional data structures (images) and setting their values to zero
a = np.zeros(shape=(6, 6))
a[0,0] = 2       # assign value by index
a[1:3, 0:4] = [[0,1,2,3], [2,3,4,5]]  # assign value by slicing