
def if_perfect_num(list):
    return list[19] == sum(filter(lambda x: x % list[19] == 0, range(1, list[19])))
