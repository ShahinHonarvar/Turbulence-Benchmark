
def sum_of_divisors_in_range(num):
   return sum(divisor for divisor in range(27, 45) if num % divisor == 0)
