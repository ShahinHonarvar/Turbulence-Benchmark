
def if_perfect_num(lst):
    return lst[6] == sum([i for i in range(1, lst[6]) if lst[6] % i == 0])
