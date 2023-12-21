
def all_odd_ints_exclusive(numbers):
    return [number for number in numbers if number % 2 != 0 and number < max(numbers)]
