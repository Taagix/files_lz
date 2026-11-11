import docx
import pandas as pd

doc = docx.Document('Война и мир.docx')
text = '\n'.join(para.text.lower() for para in doc.paragraphs)
all_world = []
df1 = xl.parse('Частотный список')
df1