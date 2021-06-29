# テキストファイルを訳してくれる
from googletrans import Translator
import sys

args= sys.argv
if len(args) < 2:
    print('Command should be like')
    print('python3 googlefiletranlate.py textfile.txt')
else:
    with open(args[1], encoding='utf-8_sig') as f:
      print(f)
      lines = f.readlines()

    translator = Translator()
    for line in lines:
        translated = translator.translate(line, dest="ja");
        print(line)
        print(translated.text)
        print()
    print('finished')