#                        Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#                        Пример:
#                        - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)




# N = int(input('введите число '))
# a=1
# mass= []
# for i in range(1,N+1):
#     a=a*i
#     mass.append(a)
# print(mass)
    





#                        Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#                        Пример:
#                       - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



# n= int(input('введите число '))
# my_list={}
# sum=0
# for i in range(1,n+1):
#     my_list[i] = (1+1/i)**i
#     sum+=my_list[i]
# sum=round(sum,3)
# print(sum)   



#                                             Реализуйте алгоритм перемешивания списка.

# import random
# my_list = [1,2,3,4,5,6]
# random.shuffle(my_list)
# print(my_list)