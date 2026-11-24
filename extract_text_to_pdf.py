from PyPDF2 import PdfReader

reader = PdfReader("my_resume (2).pdf")
page = reader.pages[0]
print(page.extract_text())