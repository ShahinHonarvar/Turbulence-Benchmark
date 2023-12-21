
def all_odd_ints_inclusive(lst):
    odds = [x for i, x in enumerate(lst[21:98]) if x % 2 != 0]
    return odds
