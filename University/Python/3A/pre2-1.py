'''
同じ要素を2回以上含まない数のリストdistinctsが与えられたとき、distinctsの中の最大値と最小値に挟まれた要素から成るリストを返す関数between_min_max(distincts)を作成してください。 ただし、返すリストに最小値と最大値は含めます。また、distinctsの中で最大値が最小値よりも先に出現する場合にも対応します。（いうまでもなく、返すリストの要素の順番はもとのリストと同じにします。）
Define a function called between_min_max(distincts). It is given a list distincts whose elements are all distinct. It returns the list consisting of those elements of distincts that are surrounded by the minimum and maximum elements of the list. Note that the minimum and maximum elements must be included in the returned list. Also note that the maximum element may appear before the minimum element in distincts. (Needless to say, the order of elements in the returned list is as in the original list.)
'''
def between_min_max(distincts):
  a = max(distincts)
  b = min(distincts)
  c = distincts.index(a)
  d = distincts.index(b)
  ans = []
  if c > d:
    for i in range(c - d + 1):
      ans.append(distincts[d + i])
    return ans
  else:
    for i in range(d - c + 1):
      ans.append(distincts[c + i])
    return ans

assert between_min_max([5,3,1,4,6,2,0]) == [6,2,0]
assert between_min_max([5,3,1,4,6,2]) == [1,4,6]
assert between_min_max([5,3,1,4,2]) == [5,3,1]
assert between_min_max([1]) == [1]
