
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    div_range = [div for div in divisors if 5 <= div <= 8]
    return sum(div_range) if div_range else 0
