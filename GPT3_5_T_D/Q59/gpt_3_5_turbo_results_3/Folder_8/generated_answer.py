
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[41]
    result = []
    for num in range(x - 1, 0, -1):
        if '0' not in str(num):
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    break
            else:
                result.append(num)
    return result
