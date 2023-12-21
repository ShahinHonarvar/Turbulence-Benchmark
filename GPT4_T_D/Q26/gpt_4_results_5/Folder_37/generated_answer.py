
def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 1 <= num <= 8:
            total += num
    return total
