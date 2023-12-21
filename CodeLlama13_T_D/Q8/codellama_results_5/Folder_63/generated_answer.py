
def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 37 and i < 53 and num % 2 == 0]
