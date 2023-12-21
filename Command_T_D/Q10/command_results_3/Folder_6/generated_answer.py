def all_odd_ints_exclusive(ints):
    odds = [x for x in range(86, 100) if x % 2 == 1]
    return [x for x in ints[odds[0]:odds[-1] + 1]]
