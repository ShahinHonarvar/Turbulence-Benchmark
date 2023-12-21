
def sum_of_divisors_in_range(n):
    current_sum = 0
    for i in range(84, 87):
        if n % i == 0:
            current_sum += i
    return current_sum
