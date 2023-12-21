
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return sum(div for div in divisors if 19 <= div <= 69)
