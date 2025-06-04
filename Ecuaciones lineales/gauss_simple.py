import numpy as np

#Instanciar la matriz y el vector
matrixA = np.array([[-3, 2, 1],[6, -8, -2],[1, -1, -2]])
matrixA = matrixA.astype(float)

vectorB = np.array([2, 1, 3])
vectorB = vectorB.astype(float)

#gauss sin pivoteo
def gauss(matrix, vector):
  n = len(vector)
  for col in range(n - 1):
    for row in range(col + 1, n):
      lam = (matrix[row][col])/(matrix[col][col])
      matrix[row] = matrix[row] - matrix[col]*lam
      vector[row] = vector[row] - vector[col]*lam

  x = np.zeros(n)
  for col in range(n-1, -1, -1):
    x[col] = (vector[col] - np.dot(matrix[col, col+1:n], x[col+1:n]))/(matrix[col][col])
  print(x)



gauss(matrixA, vectorB)
