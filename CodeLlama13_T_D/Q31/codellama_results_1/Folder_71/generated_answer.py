
def if_perfect_num(lst):
    return lst[78] == sum(filter(lambda x: x % lst[78] == 0, range(1, lst[78])))
