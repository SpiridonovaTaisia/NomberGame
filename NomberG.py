from random import randint

x = randint(1, 10)
attempt = 3

while attempt > 0:
    print("Я загадал число от 1 до 10:")
    user_num = int(input("Ваша догадка: "))
    if user_num == x:
         print(f"Ты угадал число, молодец!\nКоличество твоих попыток:{attempt}\n Спасибо за игру")
         break
    else:
        print("Вы не угадали")
        attempt -= 1