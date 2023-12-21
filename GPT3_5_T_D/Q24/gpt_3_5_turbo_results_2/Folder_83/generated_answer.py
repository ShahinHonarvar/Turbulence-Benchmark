
def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for i in range(1, num+1):
        if num % i == 0 and 5 <= i <= 7:
            divisor_sum += i
    return divisor_sum
