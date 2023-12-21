
def if_perfect_num(lst):
    return lst[162] == sum(range(1, int(sqrt(lst[162]))+1)) and all(lst[162] % i == 0 for i in range(2, int(sqrt(lst[162]))+1))
