
def sum_of_divisors_in_range(n):
   return sum(i for i in range(1, n+1) if n % i == 0 and 5 <= i <= 8)
