
def sum_of_divisors_in_range(n):
    def is_divisor(n, divisor):
        return n % divisor == 0

    sum_of_divisors = 0
    for i in range(14, 49):
        if is_divisor(n, i):
            sum_of_divisors += i

    return sum_of_divisors
