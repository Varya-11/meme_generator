# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(i)
#
#
#
#
#
# total = 0
# number = int(input())
# for i in range(1, number + 1):
#      if i % 3 == 0:
#         total += i
# print(total)
from unicodedata import numeric

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         total += i ** i
#     else:
#         total -= i ** i
# print(total)


# n = int(input())
# prev = 1
# curr = 1
# print(curr, prev, end = ' ')
# while curr <= n:
#     next =  curr + prev
#     print(next, end = ' ')
#     prev = curr
#     curr = next

#
# n = int(input())
# x = float(input())
















from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')
top_text = input('Введите верхний текст: ')
bottom_text = input('Введите нижний текст: ')
print(top_text, bottom_text, end = '')

print('Список картинок: ')
print('1. Кот в ресторане')
print('2. Кот в очках')
image_number = int(input('Введите номер картинки: '))
if image_number == 1:
    image_file = 'Кот в ресторане.png'
elif image_number == 2:
    image_file = 'Кот в очках.png'

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size = 70)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill='black')

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill='black')


image.save('new_meme.jpg')




