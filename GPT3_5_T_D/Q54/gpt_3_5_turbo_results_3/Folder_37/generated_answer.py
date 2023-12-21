
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[35]
    result = []
    for num in range(x - 1, 1, -1):
        truncatable = True
        n = num
        while truncatable and n > 0:
            if not is_prime(n):
                truncatable = False
            n //= 10
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)
