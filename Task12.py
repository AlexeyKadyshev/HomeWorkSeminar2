# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

from math import sqrt, pow
summa = 0
while summa != '0000':
    print("Для завершения программы введите: 0000 ")
    summa = input("Введите сумму чисел: ")
    if summa == '0000':
        print("До свидания")
        break
    summa = int(summa)
    product = int(input("Введите произведение чисел: "))
    if summa < 0 or product < 0:
        print("Введены некорректные значения")
    else:
        # Приводим условие к квадратному уравнению:
        # summa = num1 + num2 => num2 = summa - num1
        # product = num1 * num2 => num2 = product / num1
        # summa - num1 = product / num1
        # num1 * (summa - num1) = product
        # num1^2 - summa * num1 + product = 0
        dis = pow(summa, 2) - 4 * product
        num1 = (summa - sqrt(dis)) / 2
        num2 = (summa + sqrt(dis)) / 2
        print(f"Загаданные числа равны {int(num1)} и {int(num2)}")