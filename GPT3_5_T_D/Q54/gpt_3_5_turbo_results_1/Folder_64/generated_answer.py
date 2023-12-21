
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[4]
    result = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                result.append(i)
    return sorted(result)
