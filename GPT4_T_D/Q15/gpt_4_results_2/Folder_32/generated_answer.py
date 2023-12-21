
def sum_odd_ints_inclusive(numbers):
    start, end = 21, 97
    return sum(num for num in numbers[start:end+1] if num % 2 != 0)
