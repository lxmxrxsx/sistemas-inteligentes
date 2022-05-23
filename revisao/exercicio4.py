def addNumberToList(list, number):
    if(number in list):
        return list
    else:
        list.append(number)
        return list


list = [1, 2, 3, 4, 5, 6, 7]
print(list)
print(addNumberToList(list, 7))
print(addNumberToList(list, 8))
