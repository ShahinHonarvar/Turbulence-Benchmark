
def sum_even_ints_inclusive(numbers):
    if len(numbers) < 56:
        return 0
    else:
        even_sum = sum(i for i in numbers[34:56] if i % 2 == 0)
        return even_sum
