
def if_perfect_num(lst):
    return sum([i for i in range(1, lst[828]//2 + 1) if lst[828] % i == 0]) == lst[828]
