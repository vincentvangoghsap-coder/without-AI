'''
[('+', 3), ('-', 5), ('+', 2), ('+', 1), ('-', 10)] のように、 演算子の文字列（+ または -）と整数からなるタプルを格納したリスト lp が与えられたとき、 初期値 0 に対して、リストの各タプルの演算子と整数を順に適用して得られる結果を返す関数 calculate_ops(lp) を定義する。
たとえば、lp が上の例の場合、calculate_ops(lp) は 0+3-5+2+1-10 の計算結果を返します。
Define a function calculate_ops(lp) that is given a list of tuples lp, such as [('+', 3), ('-', 5), ('+', 2), ('+', 1), ('-', 10)], with each tuple consisting of an operator string (+ or -) and an integer. It returns the value obtained by successively applying the operator and the integer in each tuple to the initial value 0.
For example, if lp is as above, calculate_ops(lp) returns the result of calculating 0+3-5+2+1-10.
'''

def calculate_ops(lp):
    a = 0
    for i in range(len(lp)):
        if lp[i][0] == '+':
            a += lp[i][1]
        else:
            a -= lp[i][1]
    return a
assert calculate_ops([('+', 3), ('-', 5), ('+', 2), ('+', 1), ('-', 10)]) == -9
assert calculate_ops([('-', 1), ('-', 2), ('-', 3)]) == -6
assert calculate_ops([('+', 1), ('+', 2), ('+', 3)]) == 6
assert calculate_ops([]) == 0
