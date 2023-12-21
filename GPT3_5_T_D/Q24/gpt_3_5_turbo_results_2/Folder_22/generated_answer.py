
def sum_of_divisors_in_range(num):
   divisors = [i for i in range(1, num + 1) if num % i == 0 and 4 <= i <= 7]

   if divisors:
       return sum(divisors)
   else:
       return 0
