import zbar
from PIL import Image 

scanner = zbar.ImageScanner()
pil = Image.open('20180520_170027_2.jpg').convert('L')
width, height = pil.size
raw = pil.tobytes()
image = zbar.Image(width, height, 'Y800', raw)
result = scanner.scan(image)

for symbol in image:
    print symbol.data.decode(u'utf-8')     # 1639
