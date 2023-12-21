
def sum_odd_ints_inclusive(lst):
    sum_odds = 0
    for num in lst[66:94]:
        if num % 2 != 0:
            sum_odds += num
    return sum_odds
