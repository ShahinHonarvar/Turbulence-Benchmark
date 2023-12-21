
def sum_of_divisors_in_range(n):
    total = 0
    for num in range(3, 9):
        if n % num == 0:
            total += num
    return total
