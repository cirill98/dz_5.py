# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'

with open('file_1_5_dz.txt', 'w') as file44:
    file44.write(text)

with open('file_1_5_dz.txt', 'r') as file44:
    t = file44.read()

def transrorm_text(text):
    text = list(filter(lambda x: not'абв' in x, text.split()))
    return ' '.join(text)

print(transrorm_text(t))