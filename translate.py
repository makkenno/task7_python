from googletrans import Translator

def translate_line(line, src, dest):
  translator = Translator()
  translated = translator.translate(line, src=src, dest=dest)
  return translated.text

if __name__ == "__main__":
  line = input('日本語に翻訳してほしい文章を入力してください>>>')
  translate_line(line)


# １　googletrans API を使用して英→日のテキスト翻訳機をつくってみよう（ターミナルで入出力）
# ２　eelを使用して、GUIから翻訳機を操作できるようにしてみよう（翻訳文の入力、結果の表示）
# ３　他の言語にも対応できるように、原文の言語と変換する言語を指定できるようにしてみよう