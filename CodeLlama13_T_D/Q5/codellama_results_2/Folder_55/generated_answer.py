
def all_neg_ints_inclusive(numbers):
    return [n for n in numbers if n < 0 and abs(n) <= 10]
