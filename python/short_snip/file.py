
text_string = "Text"

#### Open file for write
f = open('text.txt', 'w') # открываем для записи (writing)
f.write(text_string) # записываем текст в файл
f.close() # закрываем файл

#### Read from file
f = open('text.txt') # если не указан режим, по умолчанию подразумевается
while True:
  line = f.readline()
  if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
    break
  print(line, end='')
  f.close() # закрываем файл
