
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[945]
    result = []
    for i in range(x - 1, 1, -1):
        digits = str(i)
        if '0' not in digits and all(is_prime(int(digits[:j])) for j in range(1, len(digits) + 1)):
            result.append(i)
    return result
