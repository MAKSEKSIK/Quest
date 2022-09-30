import random
Length = 10
Health = 100
Respect = 20
Weight = 30
print("Ваша цель: Добиться уважения больше 100 и не дать основным параметрам упасть до нуля")
while Length > 0 and Health > 0 and Respect > 0 and Weight > 0:
    print("Ваши характеристики:")
    print("Длина норы:", Length)
    print("Здоровье:", Health)
    print("Уважение:", Respect)
    print("Вес:", Weight)
    print()
    print("Что хотите сделать?")
    print("1. Копать нору")
    print("2. Поесть травы")
    print("3. Подраться")
    print("4. Проспать весь день")

    a = int(input())
    if a == 2:
        print("1. Жулхой")
        print("2. Зелёной")
        b = int(input())
        if b == 1:
            Health += 10
            Weight += 15
        if b == 2:
            if Respect < 30:
                Health -= 30
            if Respect >= 30:
                Health += 30
                Weight += 30
    if a == 1:
        print("1. Интенсивно")
        print("2. Лениво")
        b = int(input())
        if b == 1:
            Length += 5
            Health -= 30
        if b == 2:
            Length += 2
            Health -= 10
    if a == 4:
        Length -= 2
        Health += 20
        Respect -= 2
        Weight -= 5
    if a == 3:
        print("1. Со слабым существом")
        print("2. Со средним существом")
        print("3. С сильным существом")
        b = int(input())
        if b == 1:
            c = 30
            summ = Weight + c
            d = random.randint(1, Weight + c)
            if d <= Weight:
                print("Ты выиграл")
                Respect += 10
            else:
                print("Ты проиграл")
                Health -= 10
        if b == 2:
            c = 50
            summ = Weight + c
            d = random.randint(1, Weight + c)
            if d <= Weight:
                print("Ты выиграл")
                Respect += 20
            else:
                print("Ты проиграл")
                Health -= 20
        if b == 3:
            c = 70
            summ = Weight + c
            d = random.randint(1, Weight + c)
            if d <= Weight:
                print("Ты выиграл")
                Respect += 40
            else:
                print("Ты проиграл")
                Health -= 40
    if a == 4:
        Length -= 2
        Health += 20
        Respect -= 2
        Weight -= 5
    print("Наступила ночь")
    Length -= 2
    Health += 20
    Respect -= 2
    Weight -= 5
if Respect >= 100:
    print("Вы прошли игру")
if (Health <= 0 or Weight <= 0 or Respect <= 0 or Length <= 0):
    print("Вы всё проиграли")
