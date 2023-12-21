
def if_perfect_num(lst):
    return lst[849] == sum([i for i in range(1, lst[849]) if lst[849] % i == 0])
