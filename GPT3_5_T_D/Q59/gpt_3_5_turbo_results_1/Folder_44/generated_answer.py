
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if "0" in str(num):
            return False
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:])
        return True

    x = nums[39]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)
