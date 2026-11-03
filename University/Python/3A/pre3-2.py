'''
文字列sと辞書dが与えられたとき、sの各文字cを見ていって、cがdのキーとして登録されていたら、辞書dの中のキーcの値を1増やす関数inc_freq(s, d)を定義してください。（dに新たなキーを登録してはいけません。）
この関数は、引数の辞書の中身を関数内部で更新します。返り値を返す必要はありません。
Define a function inc_freq(s, d) such that given a string s and a dictionary d, it checks each character c in s and increments the value of key c in dictionary d by 1 if c is recorded as a key in d. (You are not allowed to record a new key in d.)
This function updates the contents of the dictionary given as an argument. It does not need to return a value.
'''
def inc_freq(s, d):
  for i in range(len(s)):
    if s[i] in d:
      d[s[i]] += 1
