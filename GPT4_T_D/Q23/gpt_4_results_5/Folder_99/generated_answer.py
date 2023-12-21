
def find_divisors_in_range(n):
    divisors_range = []
    for i in range(378, 783):
        if n % i == 0:
            divisors_range.append(i)
    return divisors_range
