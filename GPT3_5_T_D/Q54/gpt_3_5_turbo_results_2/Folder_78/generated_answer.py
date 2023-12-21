
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def all_right_truncatable_prime(numbers):
  x = numbers[23]
  right_truncatable_primes = []

  for num in range(2, x):
    if is_prime(num):
      is_right_truncatable = True
      for i in range(1, len(str(num))):
        truncated_num = int(str(num)[:-i])
        if not is_prime(truncated_num):
          is_right_truncatable = False
          break
      if is_right_truncatable:
        right_truncatable_primes.append(num)
  
  return sorted(right_truncatable_primes)
