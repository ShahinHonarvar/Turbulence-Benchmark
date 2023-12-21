
def all_left_truncatable_prime(nums):
  from sympy import isprime

  def is_left_truncatable(n):
    if '0' in str(n):
      return False

    for i in range(len(str(n))):
      if not isprime(int(str(n)[i:])):
        return False

    return True

  x = nums[70]
  results = [i for i in range(2, x) if is_left_truncatable(i)]
  return sorted(results, reverse=True)
