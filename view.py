import eel
import desktop
from translate import translate_line

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def translate(line):
  translated_text = translate_line(line)
  eel.displayText(translated_text)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)