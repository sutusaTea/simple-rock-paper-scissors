import random
person = input("камень, ножницы, бумага? ")
pc = random.random()
if 0 < pc < 0.3:
    pc = "камень"
else:
    if 0 < pc < 0.6:
        pc = "ножницы"
    else:
        if 0 < pc < 0.9:
            pc = "бумага"

if person == "камень" and pc == "ножницы":
    print("Поздравляю! Ты выйграл!")

if person == "ножницы" and pc == "бумага":
    print("Поздравляю! Ты выйграл!")

if person == "бумага" and pc == "камень":
    print("Поздравляю! Ты выйграл!")

if person == pc:
    print("Ничья! Давай еще раз!")

if person == "ножницы" and pc == "камень":
    print("Поздравляю! Ты проиграл!")

if person == "камень" and pc == "бумага":
    print("Поздравляю! Ты проиграл!")

if person == "бумага" and pc == "ножницы":
    print("Поздравляю! Ты проиграл!")

if person != "ножницы" and person != "бумага" and person != "камень":
    print("Нет, нет, нет, ты кажется не понял. Тебе надо вести либо камень, либо ножницы, либо бумага!")