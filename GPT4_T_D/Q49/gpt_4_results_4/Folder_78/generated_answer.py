
def if_decimal_is_divisible(binary_string):
   def fibonacci(n):
       a, b = 0, 1
       for _ in range(n):
           a, b = b, a + b
       return a
   
   num = int(binary_string, 2)
   fib_115 = fibonacci(115)
   
   return num % fib_115 == 0
