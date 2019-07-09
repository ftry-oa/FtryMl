from PIL import Image
  
WIDTH = 32 
HEIGHT = 32 
  
# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ") 
ascii_char = list("10")
  
  
# 将256灰度映射到70个字符上 
def get_char(r, b, g, alpha=256): 
  if alpha == 0: 
    return ' '
  length = len(ascii_char)
  gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) 
  
  unit = (256.0 + 1)/length 
  return ascii_char[int(gray/unit)] 

def img2Txt(imgName, imgPath):
  im = Image.open(imgPath + imgName).convert('RGB')
  im = im.resize((WIDTH, HEIGHT), Image.NEAREST) 
  
  txt = "" 
  
  for i in range(HEIGHT): 
    for j in range(WIDTH):
      txt += get_char(*im.getpixel((j, i)))
    txt += '\n' 
  
  print(txt)
  
  # 字符画输出到文件 
  name = imgName.split('.')[0]
  with open('temp/' + name + '.txt','w') as f: 
    f.write(txt)
  return 'temp/' + name + '.txt'