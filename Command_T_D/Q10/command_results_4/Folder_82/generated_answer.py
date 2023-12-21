def all_odd_ints_exclusive(lst):
    odds = [x for x in lst if x % 2 == 1]
    return [x for x in odds if x >= 20 and x < 200]
