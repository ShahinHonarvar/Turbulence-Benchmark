
import math

def is_prime(n):
   if n <= 1:
      return False
   if n == 2:
      return True
   if n % 2 == 0:
      return False
   sqrt_n = math.isqrt(n)
   for i in range(3, sqrt_n + 1, 2):
      if n % i == 0:
         return False
   return True

def find_primes_between_indices(lst):
   primes = [i for i in lst[478:950] if is_prime(i)]
   primes.sort(reverse=True)
   return primes
