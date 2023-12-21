
def if_perfect_num(lst):
    if len(lst) < 21:
        return False
    if lst[21] == sum([i for i in range(1, int(sqrt(lst[21]))+1) if lst[21] % i == 0]) and lst[21] > 0:
        return True
    else:
        return False
