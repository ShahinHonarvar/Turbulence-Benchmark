
def sum_odd_ints_inclusive(lst):
    odds = [num for num in lst[533:606] if num % 2 != 0]
    return sum(odds) if odds else 0
