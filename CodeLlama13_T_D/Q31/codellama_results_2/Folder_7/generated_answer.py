
def if_perfect_num(lst):
    return lst[851] == sum(filter(lambda x: x % lst[851] == 0, range(1, lst[851])))
