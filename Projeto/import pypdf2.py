import PyPDF2 
import os

#variavél que ira fundir, mesclar os pdfs
merger = PyPDF2.PdfMerger() 
#listdir lista um directorio/pasta 
lista_arq = os.listdir("pdf")
lista_arq.sort()
print(lista_arq)

for pdf in lista_arq:
    if ".pdf" in pdf:
        merger.append(f"pdf/{pdf}")

merger.write("PDF mesclado pronto.pdf")