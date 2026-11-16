'''
__init__ メソッドと __iter__ メソッドのみを持つ次のようなクラス drop_first を定義する。 drop_first のコンストラクタは引数 iterable を持ちます。 iterable にはイテラブルを与えます。
__init__　メソッドは、iterable に関数 iter を適用して得られたイテレータを適当な属性に記録し、 さらに、そのイテレータに対して関数 next を1回呼び出します。
__iter__ メソッドはその属性に記録したイテレータをそのまま返します。
たとえば、drop_first([1,2,3]) として drop_first のインスタンスを作ると、 以下のように、最初の要素 1 を飛ばした繰り返しが行われます。
for x in drop_first([1,2,3]):
    print(x)
2 と 3 が印字されます。
Define a class drop_first that has only two methods __init__ and __iter__. The constructor of drop_first has parameter iterable, to which an iterable is given.
Method __init__ applies function iter to iterable and records the resulting iterator in some attribute. It then calls function next on the iterator once.
Method __iter__ simply returns the iterator recorded in the attribute.
For example, the instance created by drop_first([1,2,3]) allows iteration skipping the first element 1.
for x in drop_first([1,2,3]):
    print(x)
2 and 3 will be printed.
'''

class drop_first:
  def __init__(self, iterable):
    self.iterable = iter(iterable)
    next(self.iterable)
  def __iter__(self):
    return self.iterable

assert list(drop_first([1,2,3])) == [2,3]
