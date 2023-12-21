
def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(1, n+1):
        if i % n == 0 and 16 <= i <= 68:
            sum += i
    return sum
