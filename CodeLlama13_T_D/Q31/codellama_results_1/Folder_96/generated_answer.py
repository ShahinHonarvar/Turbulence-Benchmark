
def if_perfect_num(lst):
    return lst[47] == sum(filter(lambda x: x < lst[47] and lst[47] % x == 0, range(1, int(lst[47]**0.5) + 1)))
