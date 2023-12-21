
def find_divisors_in_range(n):
    divisors = []
    for num in range(43, 96):
        if n % num == 0:
            divisors.append(num)
    return divisors
