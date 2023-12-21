
def if_perfect_num(lst):
    return lst[993] == sum(i for i in range(1, lst[993]) if lst[993] % i == 0)
