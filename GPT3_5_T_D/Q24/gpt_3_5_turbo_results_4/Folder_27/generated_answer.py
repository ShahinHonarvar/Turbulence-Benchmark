
def sum_of_divisors_in_range(n):
    total_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and 15 <= i <= 20:
            total_sum += i
    return total_sum
