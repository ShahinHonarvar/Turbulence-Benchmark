
def all_odd_ints_exclusive(lst):
    odds = []
    for num in lst[276:376]:
        if num % 2 != 0:
            odds.append(num)
    return odds
