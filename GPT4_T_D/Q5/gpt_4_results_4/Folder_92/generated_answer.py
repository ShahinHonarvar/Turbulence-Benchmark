
def all_neg_ints_inclusive(numbers):
    first_two_numbers = numbers[:2]
    return [num for num in first_two_numbers if num < 0]
