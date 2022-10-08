# ПРИВЕТСТВИЕ НА РЕКУРСИИ
# name = str(input())

# def greet(name):
#     print ("hello, " + name + "!")
#     greet2(name)
#     print ("getting ready to say bye...")
#     bye()

# def greet2(name):
#     print ("how are you," + name + "?")

# def bye():
#     print("ok bye!")


# greet(name)






# РЕКУРСИВНЫЙ МЕТОД ПОДСЧЕТА ФАКТОРИАЛА
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x* fact(x-1)

# print(fact(7))





# ОБЫЧНЫЙ МЕТОД ПОДСЧЕТА ЭЛЕМЕНТОВ
# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

# print(sum([1,2,3,4]))




# РЕКУРСИВНЫЙ МЕТОД ПОДСЧЕТА ЭЛЕМЕНТОВ
# def sum(arr):
#     if not arr:
#         return 0
#     else:
#         return arr[0] + sum(arr[1:])

# print(sum([1,2,3,4]))





# НАХОЖДЕНИЕ НАИБОЛЬШЕГО ЧИСЛА В СПИСКЕ
# def maxn(arr):
#     max = arr[0]
#     for i in range(arr):
#         if arr[i] > max:
#             max = arr[i]
#     return max

# print(max([1222,7,23,405]))    