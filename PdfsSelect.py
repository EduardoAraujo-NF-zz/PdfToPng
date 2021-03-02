import sys
import os
from PyPDF2 import PdfFileReader, PdfFileMerger

# Salva cada argumento do comando em uma lista
# Argumento[0] se trata do comando

# Contagem de numero de argumentos
# Visivel apenas no console para debug
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"Argument {i:>6}: {arg}")

# captura diretorio atual
files_dir = "./"


merger = PdfFileMerger()
for filename in sys.argv[1:]:
    merger.append(PdfFileReader(os.path.join(files_dir, filename)))

# Salva em um arquivo chamado "000Fullpdfs.pdf"
merger.write(os.path.join(files_dir, "000Fullpdfs.pdf"))
