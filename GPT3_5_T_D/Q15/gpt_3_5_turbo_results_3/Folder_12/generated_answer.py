
def sum_odd_ints_inclusive(lst):
    odds = []
    for num in lst[14:65]:
        if num % 2 != 0:
            odds.append(num)
    return sum(odds) if odds else 0
