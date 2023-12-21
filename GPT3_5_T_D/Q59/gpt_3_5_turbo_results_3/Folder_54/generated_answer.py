
def all_left_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = nums[88]
    result = []

    for num in range(x, 0, -1):
        if '0' in str(num):
            continue
        truncatable = True
        while num > 0:
            if not is_prime(num):
                truncatable = False
                break
            num //= 10
        if truncatable:
            result.append(num)

    return sorted(result, reverse=True)
