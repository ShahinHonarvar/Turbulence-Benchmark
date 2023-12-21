
def if_perfect_num(lst):
    return lst[85] == sum(filter(lambda x: x % 2 == 0, range(1, int(sqrt(lst[85])))))**2
