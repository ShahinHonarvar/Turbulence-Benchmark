
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[433]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and all(is_prime(int(str(num)[:-i])) for i in range(1, len(str(num)))):
            result.append(num)
    return sorted(result, reverse=True)
