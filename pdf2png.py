import sys
import os
from pdf2image import convert_from_path

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv[1:]):
        print(f"Extraindo imagens do arquivo: {arg}")

pages = convert_from_path(sys.argv[1], 300)

#Saving pages in jpeg format
i = 1
for page in pages:
    page.save(f'page{i}.jpg', 'JPEG')
    i = i+1
