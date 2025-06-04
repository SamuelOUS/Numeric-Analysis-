import numpy as np

#Instanciar la matriz y el vector
matrixA = np.array([[0, 2, 1],[6, -8, -2],[1, -1, -2]])
matrixA = matrixA.astype(float)

vectorB = np.array([2, 1, 3])
vectorB = vectorB.astype(float)

#gauss con pivoteo
def gauss_pivot(matrix, vector):
  n = len(vector)
  for col in range(n - 1):
    if matrix[col][0] == 0 and matrix[col+1][0] != 0:
      matrix[[col, col+1]] = matrix[[col+1,col]]
      vector[[col, col+1]] = vector[[col+1,col]]
    #print(matrix)
    for row in range(col + 1, n):
      lam = (matrix[row][col])/(matrix[col][col])
      matrix[row] = matrix[row] - matrix[col]*lam
      vector[row] = vector[row] - vector[col]*lam
  #print(matrix)
  x = np.zeros(n)
  for col in range(n-1, -1, -1):
    x[col] = (vector[col] - np.dot(matrix[col, col+1:n], x[col+1:n]))/(matrix[col][col])
  print(x)
  return x



gauss_pivot(matrixA, vectorB)


matrixA = np.array([[0.003000, 59.14],[5.291, -6.130]])
matrixA = matrixA.astype(float)

vectorB = np.array([10, 1])
vectorB = vectorB.astype(float)

gauss_pivot(matrixA, vectorB)
