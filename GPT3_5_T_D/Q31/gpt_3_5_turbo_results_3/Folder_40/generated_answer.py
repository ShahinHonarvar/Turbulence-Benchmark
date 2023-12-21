
def if_perfect_num(numbers):
   def is_perfect(num):
      divisors = []
      for i in range(1, num):
         if num % i == 0:
            divisors.append(i)
      if sum(divisors) == num:
         return True
      return False
  
   if len(numbers) < 8:
      return False
   if is_perfect(numbers[7]):
      return True
   return False
