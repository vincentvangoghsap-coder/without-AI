'''
行列 matrix を受け取り、その転置行列を返す関数 transpose を定義せよ。
Define a function transpose that takes a matrix matrix and returns a transpose.
'''

def transpose(matrix):
  if matrix == []:
    return []
  else:
    nr_rows = len(matrix)
    nr_cols = len(matrix[0])
    transposed_matrix = [[] for i in range(nr_cols)]
    for i in range(nr_cols):
      for _ in range(nr_rows):
        transposed_matrix[i].append(0)
    for i in range(nr_rows):
      for j in range(nr_cols):
        transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
assert transpose([]) == []
