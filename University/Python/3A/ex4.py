'''
イテラブル（たとえばリスト）xsとデータyを受け取って、xsの要素の並びをyを区切りとして分割し、分割した要素を格納したリストのリストを返す関数split_iterable(xs,y)を定義する。たとえば、
・split_iterable([1,2,0,3,4,5,0], 0) は [[1, 2], [3, 4, 5], []] を返します。
・split_iterable('/ab/c/def', '/') は、[[], ['a', 'b'], ['c'], ['d', 'e', 'f']] を返します。
・split_iterable([], 0) は [[]] を返します。
split_iterable は様々な種類のイテラブルを受け付けますが、 返値は必ずリストのリストになることに注意してください。
ファイルオブジェクトもイテラブルですので、xsがファイルオブジェクトである場合も動作するようにしてください。たとえば、xsがファイルオブジェクトで、yが文字列'\n'であるとき、xsの中の行は空白行を区切りとして分割され、空でない行のリストのリストが返されます。
Define a function split_iterable(xs,y) which splits the elements of an iterable xs using a value y as a separator, and returns the list of lists of the splitted iterable. For example,
split_iterable([1,2,0,3,4,5,0], 0) returns [[1, 2], [3, 4, 5], []].
split_iterable('/ab/c/def', '/') returns [[], ['a', 'b'], ['c'], ['d', 'e', 'f']].
split_iterable([], 0) returns [[]].
Notice that though split_iterable accepts various kinds of iterables, it always returns a list of lists.
Since a file object is an iterable, it should also work when xs is a file object. For example, if xs is a file object and y is the string '\n', then the lines in xs are split by empty lines and a list of lists of non-empty lines is returned.
'''

def split_iterable(xs, y):
  a = [[]]
  b = 0
  try:
    xs = iter(xs)
    while True:
      x = next(xs)
      if x == y:
        b += 1
        a.append([])
      else:
        a[b].append(x)
  except StopIteration:
    pass
  return a

assert split_iterable([1,2,0,3,4,5,0], 0) == [[1, 2], [3, 4, 5], []]
assert split_iterable([], 0) == [[]]
with open('gokigenyou.txt', 'w', encoding='utf-8') as f:
    f.write('こんにちは。\nごきげんよう。\n\nさようなら。\n')
try:
    with open('gokigenyou.txt', 'r', encoding='utf-8') as f:
        assert split_iterable(f, '\n') == [['こんにちは。\n', 'ごきげんよう。\n'], ['さようなら。\n']]
finally:
    import os, contextlib
    with contextlib.suppress(IOError):
        os.remove('gokigenyou.txt')
