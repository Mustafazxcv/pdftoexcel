# PDF to Excel Converter

Bu Python betiği, pytesseract ve pdf2image kütüphanelerini kullanarak PDF dosyalarını Excel dosyalarına dönüştürür.

## Gereksinimler
- pytesseract
- pdf2image
- pandas
- poppler kütüphanesi (Poppler PDF kütüphanesini yükleyin)

## Kullanım
1. `pdf_to_excel()` fonksiyonunu kullanarak PDF dosyalarını Excel'e dönüştürün.
2. PDF dosyalarının yolu ve Excel dosyasının adı parametre olarak verilmelidir.

## Örnek Kullanım
```python
from pdf_to_excel_converter import pdf_to_excel

pdf_to_excel('pdf_dosyasi.pdf', 'excel_dosyasi.xlsx')
