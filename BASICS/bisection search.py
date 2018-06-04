def bisection_search(list, e):
    if len(list) == 0:
        return False
    elif len(list) == 1:
        return list[0] == e
    else:
        half = len(list) // 2
        if e == list[half]:
            return True
        elif e > list[half]:
            return bisection_search(list[half:], e)
        else:
            return bisection_search(list[:half], e)


list1 = [0, 1.5, 2, 2.3, 4.5, 5, 6, 7, 7.4, 7.9, 8, 8.1, 9, 9.5, 10]
list2 = [5]
list3 = []
list4 = [1, 5, 9]
list5 = [0, 1.5, 2, 2.3, 4.5, 6, 7, 7.4, 7.9, 8, 8.1, 9, 9.5, 10]

print(bisection_search(list1, 5))
