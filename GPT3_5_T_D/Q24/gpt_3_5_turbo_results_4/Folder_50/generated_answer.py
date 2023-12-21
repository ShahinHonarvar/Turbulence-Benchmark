
def sum_of_divisors_in_range(n):
   if n == 0:
      return 0
   divisors = [x for x in range(1, n+1) if n % x == 0 and 57 <= x <= 86]
   if divisors:
      return sum(divisors)
   else:
      return 0
