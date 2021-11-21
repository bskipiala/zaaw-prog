def fun(list1: list, list2: list) -> list:
    listAll = list1 + list2
    set(listAll)
    listPower = []
    for element in listAll:
        listPower.append(element**3)
    return listPower

print(fun([1,2,3], [2, 3, 4, 5]))