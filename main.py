import os
import random

clear = lambda: os.system("cls")

print("привет! я загадал слово, твоя задача - угадать его.")
input("нажмите enter, чтобы продолжить:")
clear()
print("поехали!")

words = ['пирожок', 'падальщик', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

letters = []
IsWin = True 
hp = 10

while hp > 0:
    IsWin = True

    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print("*", end=" ")
            IsWin = False
        
    print()

    if IsWin: 
        print("ты угадал! молодец!")
        break

    letter = input("введите букву: ")
    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1 
        print(f"осталось попыток: {hp}")

    if hp == 0:
        print("ты проиграл. у тебя закончились попытки.")