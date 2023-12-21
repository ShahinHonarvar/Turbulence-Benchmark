
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return sum(div for div in divisors if 8 <= div <= 9)
