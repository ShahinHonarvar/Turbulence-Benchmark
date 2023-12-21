
def sum_odd_ints_inclusive(numbers):
    odd_ints = [x for x in numbers[5:8] if x % 2 == 1]
    return sum(odd_ints) or 0
