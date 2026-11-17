'''
リストのリスト matrix を受け取り、ガウスの消去法（あるいは掃き出し法とも）によって行簡約階段形 (reduced row echelon form) に変形して返却する関数 gaussian_elimination を定義する。
'''

def gaussian_elimination(matrix):
  if not matrix:
    return matrix
  nr_rows = len(matrix)
  nr_cols = len(matrix[0])
  for row in matrix:
    assert len(row) == nr_cols
  n = min(nr_rows, nr_cols)

  for i in range(n):
    pivot = abs(matrix[i][i])
    pivot_row = i
    for k in range(i + 1, nr_rows):
      if abs(matrix[k][i] > pivot):
        pivot = abs(matrix[k][i])
        pivot_row = k
    pivot_col = i
    if pivot_row != i:
      matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
    if matrix[i][i] > EPSILON:
            for j in range(i, nr_cols):
                matrix[i][j] /= pivot
        elif matrix[i][i] < -EPSILON:
            for j in range(i, nr_cols):
                matrix[i][j] /= -pivot
        else:
            for j in range(i + 1, nr_cols - 1):
                if abs(matrix[i][j]) > EPSILON:
                    pivot = matrix[i][j]
                    pivot_col = j
                    break
            if abs(matrix[i][nr_cols - 1]) > EPSILON and pivot_col == i:
                pivot = matrix[i][nr_cols - 1]
                pivot_col = nr_cols - 1
            elif pivot_col == i:
                matrix[i][nr_cols - 1] = 0

            for j in range(i + 1, nr_cols):
                if abs(pivot) > EPSILON:
                    matrix[i][j] /= pivot

        for k in range(i + 1, nr_rows):
            factor = matrix[k][pivot_col]
            for j in range(pivot_col, nr_cols):
                matrix[k][j] -= factor * matrix[i][j]

    for i in reversed(range(nr_rows)):
        j = i
        while j < nr_cols and abs(matrix[i][j]) < EPSILON:
            j += 1

        if j < nr_cols:
            for k in range(i):
                factor = matrix[k][j]
                matrix[k][j] = 0.0
                for l in range(j + 1, nr_cols):
                    matrix[k][l] -= factor * matrix[i][l]
    for i in range(nr_rows):
        for j in range(nr_cols):
            if abs(matrix[i][j]) < EPSILON:
                matrix[i][j] = 0.0

    return matrix

def max_error(m1, m2):
    ret = 0

    for i in range(max(len(m1), len(m2))):
        l1 = m1[i] if i < len(m1) else []
        l2 = m2[i] if i < len(m2) else []

        for j in range(max(len(l1), len(l2))):
            x1 = l1[j] if j < len(l1) else 0
            x2 = l2[j] if j < len(l2) else 0

            if x1 is None or x2 is None:
                pass
            else:
                ret = max(ret, abs(x1 - x2))

    return ret

matrix = [[1, 0, 2],
          [0, 1, 3]]

solution = [[1, 0, 2],
            [0, 1, 3]]

assert max_error(gaussian_elimination(matrix), solution) < 1e-12

matrix = [[4, 2, -1, 9],
          [1, 3, 1, 16],
          [1, -1, 3, 14]]

solution = [[1, 0, 0, 2],
            [0, 1, 0, 3],
            [0, 0, 1, 5]]

assert max_error(gaussian_elimination(matrix), solution) < 1e-12

matrix = [[1, 1, 1, 4],
          [2, 3, -3, 12],
          [6, -2, 5, -8]]

solution = [[1, 0, 0, 0],
            [0, 1, 0, 4],
            [0, 0, 1, 0]]

assert max_error(gaussian_elimination(matrix), solution) < 1e-12

matrix = [[4, 3, 1, 0],
          [-3, 4, 0, 1]]

solution = [[1, 0, 0.16, -0.12],
            [0, 1, 0.12, 0.16]]

assert max_error(gaussian_elimination(matrix), solution) < 1e-12

matrix = [[1, 5, 9, 13, 17],
          [2, 6, 10, 14, 18],
          [3, 7, 11, 15, 19],
          [4, 8, 12, 16, 20]]

solution = [[1, 0, None, None, None],
            [0, 1, None, None, None],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

assert max_error(gaussian_elimination(matrix), solution) < 1e-12

matrix = [[1, -8, 3, 5, 28],
          [2, -10, 3, -1, -18],
          [3, 6, -6, 3, 15],
          [4, -4, -2, 2, 0]]

solution = [[1, 0, None, 0, None],
            [0, 1, None, 0, None],
            [0, 0, 0, 1, 7],
            [0, 0, 0, 0, 0]]

assert max_error(gaussian_elimination(matrix), solution) < 1e-12

matrix = [[1, 3, -1, 6],
          [2, -2, 1, 3],
          [3, 4, -3, 3]]

solution = [[1, 0, 0, 2],
            [0, 1, 0, 3],
            [0, 0, 1, 5]]

assert max_error(gaussian_elimination(matrix), solution) < 1e-12
