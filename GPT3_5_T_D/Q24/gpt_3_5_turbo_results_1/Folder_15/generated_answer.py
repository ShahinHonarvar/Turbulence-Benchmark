
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    divisors_in_range = [d for d in divisors if 7 <= d <= 9]
    return sum(divisors_in_range)
