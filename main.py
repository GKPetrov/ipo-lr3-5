year=int(input('Введите год'))#Ввод переменных
if year%4==0 and year%100!=0:#Проверка на високосный
    print('Високосный')
elif year%400==0:#Проверка на кратность 400
    print('Високосный')
else:#Исключения
    print('Не високосный')