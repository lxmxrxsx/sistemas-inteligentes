def returnTuples(list1, list2):
    tupleList = []
    index = 0
    if len(list1) == len(list2):
        while index < len(list1):
            tupleList.append((list1[index], list2[index]))
            index += 1
        return tupleList
    return "erro"


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print(returnTuples(list1, list2))
