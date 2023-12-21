
def sum_of_divisors_in_range(num):
    divisors_in_range = [i for i in range(39,58) if num%i ==0]
    return sum(divisors_in_range) if divisors_in_range else 0
