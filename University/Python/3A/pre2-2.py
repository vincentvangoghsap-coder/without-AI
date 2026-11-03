'''
0から9までの数字から成る文字列sと、整数nが与えられたとき、sの各数字にnを加えて10で割った余りから構成される文字列を返す関数inc_digits(s,n)を定義する。たとえば、inc_digits('12', 5)は'67'という文字列を返します。inc_digits('457', 5)は'902'を返します。（5+5=10を10で割った余りは0 7+5=12を10で割った余りは2です。）数字cに対してint(c)は対応する整数を返します。逆に整数iに対してstr(i)は対応する文字列を返します。
Define a function inc_digits(s,n), which is given a string s consisting of numerals from 0 to 9 and an integer n, and returns the string consisting of the remainders of dividing the sum of each numeral in s and n by 10.
For example, inc_digits('12', 5) returns the string '67', and inc_digits('457', 5) returns '902' (the remainder of dividing 5+5=10 by 10 is 0, and that of dividing 7+5=12 by 10 is 2.)
For a digit character c, int(c) returns the corresponding integer. Inversely, for an integer i, str(i) returns the corresponding string.
'''
def inc_digits(s, n):
  a = ' '
  for i in range(len(s)):
    a += str(((int(s[i]) + n) % 10))
  return a

assert inc_digits('12', 5) == '67'
assert inc_digits('457', 5) == '902'
