#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Крестики-нолики
#Создаем два класса проверки чтобы считывать координаты и ставить крестики/нолики
class proverka1():
    def __init__(self):
            a = input("Введите координаты через пробел: ")
            b = a.split()
            x = int(b[0])
            y= int(b[1])
            while x > 3 or x < 1 or y > 3 or y < 1:#проверяем не вылезает ли за пределы
                a = input("Введите координаты еще раз через пробел: ")
                b = a.split()
                x = int(b[0])
                y= int(b[1])
            while board[x-1][y-1] != '*': #проверяем не стоит ли там уже знак
                a = input("Введите координаты еще раз через пробел: ")
                b = a.split()
                x = int(b[0])
                y= int(b[1])
            board[x-1][y-1] = 'O'
            for i in board: #выводится поле
                print(" ".join(map(str, i)))
class proverka2(): #тоже самое для крестиков
    def __init__(self):
            a = input("Введите координаты через пробел: ")
            b = a.split()
            x = int(b[0])
            y= int(b[1])
            while x > 3 or x < 1 or y > 3 or y < 1:
                a = input("Введите координаты еще раз через пробел: ")
                b = a.split()
                x = int(b[0])
                y= int(b[1])
            while board[x-1][y-1] != '*': 
                a = input("Введите координаты еще раз через пробел: ")
                b = a.split()
                x = int(b[0])
                y= int(b[1])
            board[x-1][y-1] = 'X'
            for i in board: 
                print(" ".join(map(str, i)))

board = [["*", "*", "*"],
         ["*", "*", "*"],
         ["*", "*", "*"]]# - поле
stopper = 0 #создаем переменную чтобы заканчивать цикл игры 1 - победа,2 - ничья
for i in board: #создаем поле при помощи цикла
    print(" ".join(map(str, i))) 
while stopper == 0 or (board[0][0] == '*' and board[0][1] == '*' and board[0][2] == '*' and board[1][0] == '*' 
                       and board[1][1] == '*' and board[1][2] == '*' and board[2][0] == '*' and board[2][1] == '*' 
                       and board[2][2] == '*'): #проверка продолжения игры
        if stopper != 1 and (board[0][0] == '*' or board[0][1] == '*' or board[0][2] == '*' or board[1][0] == '*'
                          or board[1][1] == '*' or board[1][2] == '*' or board[2][0] == '*' or board[2][1] == '*'
                          or board[2][2] == '*'): #проверка поля на доступность ходов
            print("Ход крестиков")
            proverka2()# обращаемся к классу для проверки 
        else:
            stopper = 2 # нужно в случае ничьи  
        #Рассматриваем разные варианты для победы 
        if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X': #выигрыш по строчкам
            print("победили крестики!")
            stopper = 1
        elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
            print("победили крестики!") 
            stopper = 1
        elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
            print("победили крестики!") 
            stopper = 1
        if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X': #выигрыш по столбцам
            print("победили крестики!")
            stopper = 1
        elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
            print("победили крестики!")
            stopper = 1
        elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
            print("победили крестики!")
            stopper = 1
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X': #выигрыш по диагоналям
            print("победили крестики!")
            stopper = 1
        elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            print("победили крестики!")
            stopper = 1
        
        if stopper != 1 and (board[0][0] == '*' or board[0][1] == '*' or board[0][2] == '*' or board[1][0] == '*'
                          or board[1][1] == '*' or board[1][2] == '*' or board[2][0] == '*' or board[2][1] == '*'
                          or board[2][2] == '*'):
            print("Ход ноликов ")
            proverka1()
        else:
            if stopper != 1: #Если выиграли крестики не обращаться к нулям
                stopper = 2 #Останавливает цикл для ничьи
        #Делаем тоже самое для проверки не выиграли ли нолики
        if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
            print("победили нолики!")
            stopper = 1
        elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
            print("победили нолики!")
            stopper = 1
        elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
            print("победили нолики!")
            stopper = 1
        if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O': 
            print("победили нолики!")
            stopper = 1
        elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
            print("победили нолики!")
            stopper = 1
        elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
            print("победили нолики!")
            stopper = 1
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O': 
            print("победили нолики!")
            stopper = 1
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            print("победили нолики!")
            stopper = 1    
if stopper == 2: #чтобы сработала ничья
    print("Ничья")


# In[ ]:




