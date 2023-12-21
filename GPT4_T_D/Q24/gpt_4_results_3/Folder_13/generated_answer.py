
def sum_of_divisors_in_range(n):
    if n < 1:
        return "Error: Input must be a positive integer."
    else:
        divisor_sum = 0
        for i in range(472, 828):
            if n % i == 0:
                divisor_sum += i
        return divisor_sum
