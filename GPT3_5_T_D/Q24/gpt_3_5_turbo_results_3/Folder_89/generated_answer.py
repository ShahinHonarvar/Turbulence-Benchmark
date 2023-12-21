
def sum_of_divisors_in_range(integer):
   total = 0
   for i in range(14, 49):
      if integer % i == 0:
         total += i
   return total
