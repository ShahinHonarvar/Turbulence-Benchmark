
def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for i in range(1, num+1):
        if num % i == 0 and 658 <= i <= 868:
            divisor_sum += i
    return divisor_sum
