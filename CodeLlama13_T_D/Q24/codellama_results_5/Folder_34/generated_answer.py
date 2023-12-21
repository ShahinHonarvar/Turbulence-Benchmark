
def sum_of_divisors_in_range(n):
    if n <= 1: return 0
    sum = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and i >= 4 and i <= 5:
            sum += i
            if n // i != i and (n//i) >= 4 and (n//i) <= 5:
                sum += n//i
    return sum
