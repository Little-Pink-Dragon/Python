with open('file_encode.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст, который необходимо сжать в формате RLE: '))
with open('file_encode.txt', 'r') as file:
    text = file.readline()
    text_com = text.split()

print(f"Текст до сжатия: {text}")

def file_encod(txt):
    enconde = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                enconde += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconde += str(count) + prev_char
        return enconde


text_com = file_encod(text)

with open('file_decode.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_com}')
print(f"Текст после сжатия: {text_com}")