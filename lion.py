import docx
import matplotlib.pyplot as plt
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.1)

document = docx.Document('Война и мир.docx')

text = ''
for abzac in document.paragraphs:
    text = text + abzac.text + ' '
text = text.lower()

znaki = ".,;:!?()[]{}«»\"'-—–\n\t"
for z in znaki:
    text = text.replace(z, ' ')

slova = text.split()

chastota_slov = {}
for s in slova:
    if s in chastota_slov:
        chastota_slov[s] = chastota_slov[s] + 1
    else:
        chastota_slov[s] = 1

spisok = []
for s in chastota_slov:
    spisok.append((chastota_slov[s], s))
spisok.sort(reverse=True)


vsego = len(slova)
f = open('word_stats.txt', 'w', encoding='utf-8')
f.write("Слово\tЧастота встречи, раз\tЧастота встречи в %\n")
for para in spisok:
    kolichestvo = para[0]
    slovo = para[1]
    procent = kolichestvo / vsego * 100
    f.write(slovo + "\t" + str(kolichestvo) + "\t" + str(round(procent, 2)) + "\n")
f.close()

print("Таблица сохранена в файл word_stats.txt")


chastota_bukv = {}
for b in text:
    if b.isalpha():
        if b in chastota_bukv:
            chastota_bukv[b] = chastota_bukv[b] + 1
        else:
            chastota_bukv[b] = 1

bukvy = sorted(chastota_bukv)
znacheniya = []
for b in bukvy:
    znacheniya.append(chastota_bukv[b])

plt.figure(figsize=(14, 6))
plt.bar(bukvy, znacheniya, color='steelblue')
plt.title('Встречаемость букв')
plt.xlabel('Буква')
plt.ylabel('Количество')
plt.show()