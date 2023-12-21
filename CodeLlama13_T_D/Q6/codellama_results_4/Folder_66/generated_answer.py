
def all_neg_ints_exclusive(numbers):
    return [x for x in numbers if x < 0 and 13 <= abs(x) < 76]
