
def all_even_ints_exclusive(numbers):
    return [x for x in numbers if x % 2 == 0 and x <= 10 and x > 0]
