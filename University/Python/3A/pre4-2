'''
ディレクトリdirpathとその中にあるテキストファイルの名前filenameを受け取って、それを文字コードcodeで開いたときの文字数を返すtext_file_len(dirpath, filename, code)を定義する。ただし、dirpathはワーキングディレクトリからの相対パスである。また、解答セルは、次の制約を満たさなければならない。
・text_file_len の中でしかファイル操作をしてはならない。
・ワーキングディレクトリを変更してはならない。
Define a function text_file_len(dirpath, filename, code) that returns the number of characters of the file named filename in directory dirpath opened with encoding code, where dirpath is a relative path from the working directory. The answer cell must satisfy the following:
・File manipulation is allowed only in text_file_len.
・The working directory is not allowed to change.
'''
def text_file_len(dirpath, filename, code):
  path = dirpath + '/' + filename
  with open(path, 'r', encoding = code) as f:
    return len(f.read())

assert text_file_len('text', 'short.txt', 'utf-8') == 5
assert text_file_len('text', 'novel.txt', 'utf-8') == 234
