
def sum_even_ints_inclusive(numbers):
    even_ints = [num for num in numbers[667:775] if num % 2 == 0]
    return sum(even_ints) if even_ints else 0
