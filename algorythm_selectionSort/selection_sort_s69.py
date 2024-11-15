"""Код сортировки массива по возрастанию"""

def findSmallest(arr):
    """Метод поиска наименьшего элемента массива"""
    smallest = arr[0]   #Переменная для хранения наименьшего значения
                            # Так как поиск будет начинаться с первого элемента,
                            # изначально пометим первый элемент, как наименьший.
    smallest_index = 0  #Индекс наименьшего значения
    for i in range(1, len(arr)):    #Перебираем индексы массива arr[], начиная со второго элемента
                                        # (т.к. первый уже был задан как наименьший)
        if arr[i] < smallest:       #Если рассматриваемый элемент меньше выбранного
            smallest = arr[i]       #Заменяем наименьший на рассматриваемый
            smallest_index = i      #Заменяем индекс наименьшего на рассматриваемый
    return smallest_index           #В конце перебора, метод возвращает индекс наименьшего

def selection_sort(arr):
    """Метод сортировки выбором, сортирует заданный в аргумент массив arr[]"""
    newArr = []     #Подготовим новый пустой массив
    for i in range(len(arr)):    #Перебираем полученный массив
        smallest = findSmallest(arr)    #Каждый раз, по новой перебираем полученный массив,
                                            # для поиска наименьшего элемента, из оставшихся.
        newArr.append(arr.pop(smallest)) #Добавляем этот элемент в конец нового массива.
                                            #При этом, удаля этот элемент, з старого массива.
    return newArr                 #Возвращаем новый массив, уже заполненный и отсортированный в порядке возрастания.

tested_arr = [5,4,7,1,11,5]    #Создаем тестовый, пока не отсортированный, массив.
sorted_arr = selection_sort(tested_arr)  #Сортируем тестовый массив, и сохраняем в переменную
print(str(sorted_arr))         #выводим отсортированный массив в консоль