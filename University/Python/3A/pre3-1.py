'''
与えられた数のリストの、最初の負数と最後の負数をタプルにして返す関数first_last_negativeを定義する。与えられた数には必ず負数が含まれると仮定して構いません。
Define a function first_last_negative which is given a list of numbers and returns a tuple of the first negative number and the last negative number in the list. You can assume that the given list contains at least one negative number.
'''
def first_last_negative(ln):
  a = []
  for i in range(len(ln)):
    if ln[i] < 0:
      a.append(ln[i])
  t = a[0], a[len(a) - 1]
  return t

assert first_last_negative([0,1,2,-3,-4,5,6,-7,-8,9,10]) == (-3,-8)
assert first_last_negative([-3]) == (-3,-3)
