import pytesseract
from pdf2image import convert_from_path
import pandas as pd

# PDF dosyasını oku ve görüntülere dönüştür
pages = convert_from_path('example2.pdf', 300)

# PDF sayfalarındaki metni tanı
text = ''
for page in pages:
    text += pytesseract.image_to_string(page)

# Metni uygun bir formata dönüştür
lines = text.split('\n')
data = [line.split('\t') for line in lines]

# Veriyi bir DataFrame'e dönüştür
df = pd.DataFrame(data)

# Excel dosyasına yaz
df.to_excel('example2.xlsx', index=False, header=False)
