def returnOcorrences(list):
    ocorrences = []
    itemsChecked = []
    for item in list:
        if item not in itemsChecked:
            count = list.count(item)
            itemsChecked.append(item)
            ocorrences.append((item, count))
    return ocorrences


list = [1, 2, 3, 4, 2, 1, 4, 23, 13, 1, 2, 4, 1, 2]
print(returnOcorrences(list))
