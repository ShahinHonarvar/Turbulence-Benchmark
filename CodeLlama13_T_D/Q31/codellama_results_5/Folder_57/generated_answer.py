
def if_perfect_num(lst):
    return lst[92] == sum([i for i in range(1, int(sqrt(lst[92]))+1) if lst[92] % i == 0])
