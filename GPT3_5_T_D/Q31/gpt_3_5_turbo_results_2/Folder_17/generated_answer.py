
def if_perfect_num(lst):
    return lst[631] == sum(i for i in range(1, lst[631]) if lst[631] % i == 0)
