'''
コワスギ銀行の裏庭では、幽霊がカボチャを育てています。あなたはカボチャたちに銀行口座を開設してあげることにしました。カボチャ用銀行口座には、開設時に名前とIDを1個ずつ割り当てます。IDの値を選ぶときは、まだIDとして使われていない正の整数のうち最小のものを採用します。はじめ、カボチャ用銀行口座はひとつも開設されていません。以下の出来事がQ回起きるので、順に処理してください。
カボチャがやってきて、名前sを名乗る。名前sが割り当てられた口座が存在する場合、そのIDを出力する。名前sが割り当てられた口座が存在しない場合、名前sの口座を新規に1個開設し、そのIDを出力する。
制約
Qは1以上2×10^5以下の整数
各出来事において、sは英小文字からなる長さ1以上10以下の文字列
入力
入力は以下の形式で標準入力から与えられる。
Q
query_1
⋮
query_Q
​
query_iはi回目の出来事を表し、以下の形式で与えられる。
s
出力
Q行出力せよ。i行目には、i回目の出来事で出力するべき値を出力せよ。
In the backyard of Kowasugi Bank, a ghost is growing pumpkins. You’ve decided to open bank accounts for the pumpkins. When opening a bank account for a pumpkin, you assign it one name and one ID. When selecting an ID value, you choose the smallest positive integer that hasn’t yet been used as an ID. Initially, no bank accounts have been opened for the pumpkins. The following event occurs Q times; please process them in order.
A pumpkin arrives and introduces itself as name s. If an account with the assigned ID s already exists, output that ID. If no account with the assigned ID s exists, open a new account for name s and output its ID.
Constraints
Q is an integer between 1 and 2×10^5, inclusive.
For each event, `s` is a string consisting of lowercase English letters, with a length between 1 and 10.
Input
The input is provided via standard input in the following format:
Q
query_1
⋮
query_Q
​
`query_i` represents the `i`-th event and is given in the following format:
s
Output
Output `Q` lines. On the `i`-th line, output the value that should be output for the `i`-th event.

Translated with DeepL.com (free version)
'''

q = int(input())
s = []
a = {}
for i in range(q):
  s.append(input())
for i in range(q):
  if s[i] in a:
    print (a[s[i]])
  else:
    a[s[i]] = len(a) + 1
    print(a[s[i]])
