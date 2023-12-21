def all_odd_ints_exclusive(lst):
    odds = [i for i in range(361, 643) if i % 2 == 1]
    return [x for x in lst[odds[0]:odds[1]] if x % 2 == 1]
