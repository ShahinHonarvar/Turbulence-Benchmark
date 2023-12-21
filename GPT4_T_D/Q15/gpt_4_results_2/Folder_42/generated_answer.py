
def sum_odd_ints_inclusive(numbers):
    required_numbers = numbers[29:80]
    odd_numbers = [num for num in required_numbers if num % 2 != 0]
    if not odd_numbers:
        return 0
    else:
        return sum(odd_numbers)
