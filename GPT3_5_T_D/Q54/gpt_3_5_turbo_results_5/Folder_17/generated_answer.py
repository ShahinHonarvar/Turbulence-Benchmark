
def all_right_truncatable_prime(nums):
  def is_prime(n):
    if n < 2:
      return False
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
    return True

  x = nums[36]
  result = []

  for num in range(x - 1, 1, -1):
    if is_prime(num):
      temp = str(num)
      for i in range(len(temp)):
        if not is_prime(int(temp[:len(temp) - i])):
          break
      else:
        result.append(num)

  return sorted(result, reverse=True)
