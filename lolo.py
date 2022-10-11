## ПРИВЕТСТВИЕ НА РЕКУРСИИ
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






## РЕКУРСИВНЫЙ МЕТОД ПОДСЧЕТА ФАКТОРИАЛА
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x* fact(x-1)

# print(fact(7))





## ОБЫЧНЫЙ МЕТОД ПОДСЧЕТА ЭЛЕМЕНТОВ
# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

# print(sum([1,2,3,4]))




## РЕКУРСИВНЫЙ МЕТОД ПОДСЧЕТА ЭЛЕМЕНТОВ
# def sum(arr):
#     if not arr:
#         return 0
#     else:
#         return arr[0] + sum(arr[1:])

# print(sum([1,2,3,4]))





## НАХОЖДЕНИЕ НАИБОЛЬШЕГО ЧИСЛА В СПИСКЕ
# def maxn(arr):
#     max = arr[0]
#     for i in range(arr):
#         if arr[i] > max:
#             max = arr[i]
#     return max

# print(max([1222,7,23,405]))    



## Метод сортировки
# def insertion_sort(nums):
#     # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         # Сохраняем ссылку на индекс предыдущего элемента
#         j = i - 1
#         # Элементы отсортированного сегмента перемещаем вперёд, если они больше
#         # элемента для вставки
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         # Вставляем элемент
#         nums[j + 1] = item_to_insert

# # Проверяем, что оно работает
# random_list_of_nums = [9, 1, 15, 28, 6]
# insertion_sort(random_list_of_nums)
# print(random_list_of_nums)




## Метод  быстрой сортировки 
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)

# random = [101, 6, 14, 10, 5, 2, 3, 808]
# print(quicksort(random)) 





# # Вывод элемента списка
# def print_items(list):
#     for i in list:
#         print(i)
#     return list

# print_items(list = [2, 4, 6, 7])




# # # Вывод элемента списка с задержкой в 1 секунду 
# from time import sleep
# def print_items2(list):
#     for i in list:
#         sleep(1)
#         print(i)
#     return list

# print_items2(list = [2, 4, 6, 7])


