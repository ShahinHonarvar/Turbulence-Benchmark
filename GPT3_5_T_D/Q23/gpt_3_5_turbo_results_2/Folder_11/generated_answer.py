
def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0 and 39 <= i <= 57:
            divisors.append(i)
    return divisors
