import pathlib
import transliterate
print(transliterate.translit('Хай Бай', reversed=True))

text = 'Вал Бал Жал'


print(transliterate.translit(text, reversed=True))


fio_kir = text
fio_lat = transliterate.translit(fio_kir, reversed=True)
print(fio_lat)