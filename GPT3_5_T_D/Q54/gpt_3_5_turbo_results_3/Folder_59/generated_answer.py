
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_right_truncatable_prime(nums):
    x = nums[84]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncatable = True
            temp = num // 10
            while temp > 0:
                if not is_prime(temp):
                    truncatable = False
                    break
                temp //= 10
            if truncatable:
                result.append(num)
    return sorted(result, reverse=True)
