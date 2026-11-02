'''
入力ファイル名filename、文字コードcode、文字の対応を表す辞書char_mapping を引数にとって、char_mappingにしたがって入力ファイル中の文字を置換したファイルを出力する関数proof_text(filename, code, char_mapping)を定義してください。ここで、入力ファイルはcodeを使って読み込み、出力ファイルは入力ファイル名の先頭に'new-'を連結した名前としてcodeを使って書き出すこと。char_mappingの値となる文字はchar_mappingのキーには含まれないと仮定してよい。
Define a function proof_text(filename, code, char_mapping) that, given an input file name filename, an encoding code, and a dictionary char_mapping of character mapping, outputs a file where characters in the input file are replaced according to char_mapping. Input files must be read with code. Output files must be written with code and named such that their names are the addition of 'new-' to the heads of the corresponding input file names. You may assume that any character in the values of char_mapping does not appear in the keys.
'''
def proof_text(filename, code, char_mapping):
  with open(filename, 'r', encoding = code) as f:
    text = f.read()
  for a, b in char_mapping.items():
    text = text.replace(a, b)
  with open('new-' + filename, 'w', encoding = code) as f:
    f.write(text)
