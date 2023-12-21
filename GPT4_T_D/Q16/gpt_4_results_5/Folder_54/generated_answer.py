
def sum_even_ints_inclusive(numbers):
    even_sum = sum(num for idx, num in enumerate(numbers) if idx in range(34, 56) and num % 2 == 0)
    return even_sum
