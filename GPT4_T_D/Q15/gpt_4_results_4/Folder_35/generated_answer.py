
def sum_odd_ints_inclusive(numbers):
    odd_numbers = [num for num in numbers[30:49] if num % 2 == 1]
    if not odd_numbers:
        return 0
    else:
        return sum(odd_numbers)
