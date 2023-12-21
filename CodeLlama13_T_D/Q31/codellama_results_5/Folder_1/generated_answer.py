
def if_perfect_num(list):
    return list[85] == sum(filter(lambda x: x % list[85] == 0, range(1, list[85])))
