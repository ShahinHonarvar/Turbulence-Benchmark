
def if_perfect_num(lst):
    return lst[7] % sum(filter(lambda x: x < lst[7], range(1, int(lst[7]) ** 0.5 + 1))) == 0
