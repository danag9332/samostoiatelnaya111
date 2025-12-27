temperature = 0 
is_rainy = "."
is_raining_heavily = "."
while True:
    print( "Что сегодня надеть")
    temperature = int(input("Напишите какая температура?\n" ))
    if temperature > 20:
        is_rainy = str(input("Есть осадки?\n"))
        if is_rainy == "да" or is_rainy == "Да":
            print("Одень футболку и шорты и дождевик\n")
        elif is_rainy == "нет" or is_rainy == "Нет": 
            print("Одень футболку и шорты\n")
        else:
            print("Вы написали что-то не то!\n")
    elif temperature < 30:
        if temperature > 0:
            is_rainy = str(input("Есть осадки?\n"))
            if is_rainy == "да" or is_rainy == "Да":
                is_raining_heavily = str(input("Сильные???\n"))
                if is_raining_heavily == "да" or is_raining_heavily == "Да":
                    print("Одень пальто и резиновые сапоги и зонт возьми\n")
                elif is_raining_heavily == "нет" or is_raining_heavily == "Нет":
                    print("Одень пальто и дождевик\n")
                else:
                    print("Вы написали что-то не то!\n")
            elif is_rainy == "нет" or is_rainy == "Нет":
                print("Одень пальто\n")
            else:
                print("Вы написали что-то не то!\n")
        else:
            print("Одень пуховик\n")
    else:
        print("Вы написали что-то не то!")