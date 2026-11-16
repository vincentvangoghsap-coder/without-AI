'''
数のリストのリストMが与えられたとき、Mの要素の要素M[i][j]のうちの最大要素mと、そのインデックスi, jを、(i, (j, m))
という形のタプルにして返す関数 find_max_indices(M) を定義する。 for文やwhile文や再帰を使わずに、内包表記や関数maxなどを使って定義することを試みる。（内包表記の中ではforを使っても構いません。）
Mは空リストではなく、Mの要素であるリストも空でないと仮定して構いません。また、Mの最大要素はMに1回のみ出現すると仮定して構いません。
Define a function find_max_indices(M) which is given a list M of lists of numbers, and returns the following tuple:(i, (j, m)) where m is the maximum element in M and M[i][j] contains m. Try to define the function not by using for-statements, while-statements or recursion, but in terms of comprehension, function max, etc. (You can use for in comprehension.)
You can assume that M is not an empty list, and elements of M are not empty lists, either. You can also assume that the maximum element of M occurs only once in M.
'''

def find_max_indices(M):
  a = [max(M[i]) for i in range(len(M))]
  m = max(a)
  i = a.index(m)
  j = M[i].index(m)
  ans = (i, (j, m))
  return ans

assert find_max_indices([[1,2,3],[9,8,7,6],[4,5]]) == (1, (0, 9))
assert find_max_indices([[1,2,3],[0,9,8,7,6],[4,5]]) == (1, (1, 9))
