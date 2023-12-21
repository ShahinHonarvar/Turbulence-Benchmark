
def if_perfect_num(lst):
    return lst[35] == sum([i for i in range(1, lst[35]) if lst[35] % i == 0])
