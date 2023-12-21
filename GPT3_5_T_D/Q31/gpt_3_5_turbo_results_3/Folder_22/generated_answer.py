
def if_perfect_num(lst):
    return lst[71] == sum(i for i in range(1, lst[71]) if lst[71] % i == 0)
