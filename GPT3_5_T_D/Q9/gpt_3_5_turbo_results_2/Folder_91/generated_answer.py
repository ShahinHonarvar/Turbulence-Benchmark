
def all_odd_ints_inclusive(lst):
    odds = []
    for num in lst[:6]:
        if num % 2 != 0:
            odds.append(num)
    return odds
