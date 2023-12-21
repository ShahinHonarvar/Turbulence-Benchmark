
def sum_even_ints_inclusive(numbers):
    even_sum = 0
    if len(numbers) >= 41:
        for i in range(28, 41):
            if numbers[i] % 2 == 0:
                even_sum += numbers[i]
    return even_sum
