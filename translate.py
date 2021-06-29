from googletrans import Translator

line = input('日本語に翻訳してほしい文章を入力してください>>>')
translator = Translator()

translated = translator.translate(line, dest="ja");
print(line)
print(translated.text)
