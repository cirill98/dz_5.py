# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Создание файла

text = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'

with open('file_4_5_dz.txt', 'w') as file_4_5:
    file_4_5.write(text)

# Извлекаем информацию из файла

with open('file_4_5_dz.txt', 'r') as f_4_5:
    cod_text = f_4_5.read()
# Кодирование

def rle_compression(data):
    compres = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                compres += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        compres += str(count) + prev_char
        return compres

compression = rle_compression(cod_text)
print(compression)

# Расшифровка

def rle_decompression(data):
    decompres = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decompres += char  * int(count)
            count = ''
    return decompres

decompression = rle_decompression(compression)
print(decompression)
