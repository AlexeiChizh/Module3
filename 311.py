x = int(input('Введите сумму вклада, руб:   '))
p = int(input('Введите годовые проценты:   '))
y = int(input('Введите желаемую сумму на счете, руб:   '))
year = 0
per = p / 100
while x <= y:
  x = x + (x * per)
  x = int(x)
  year = year + 1
print('Срок получения необходимой суммы, лет:   ', year)