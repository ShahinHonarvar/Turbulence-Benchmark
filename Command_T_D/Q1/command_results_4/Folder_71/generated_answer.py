
def all_ints_inclusive(list1):
    result = list(range(len(list1) - 1, -1, -1))
    return [list1[i] for i in result]
