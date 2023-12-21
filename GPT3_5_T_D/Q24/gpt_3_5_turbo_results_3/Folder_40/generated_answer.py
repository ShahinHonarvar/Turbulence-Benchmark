
def sum_of_divisors_in_range(n):
    return sum(num for num in range(1, n + 1) if n % num == 0 and 1 <= num <= 2)
