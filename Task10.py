# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

count_avers = 0
count_revers = 0
count_mistake = 0
count = int(input("Введите количество монет: "))
for i in range(count):
    side = input("Введите сторону монеты (орел или решка): ")
    if side == "орел":
        count_avers += 1
    elif side == "решка":
        count_revers += 1
    else:
        if side != "орел" and side != "решка":
            print("У вас монета на ребре??? Её тоже перевернем")
            count_mistake += 1
if count_avers >= count_revers + count_mistake:
    print(f"Необходимо перевернуть {count_revers + count_mistake} монет")
else:
    print(f"Необходимо перевернуть {count_avers + count_mistake} монет")
