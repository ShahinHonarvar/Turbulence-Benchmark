
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            truncated = int(str_n[i:])
            if not is_prime(truncated):
                return False
        return True

    x = nums[55]
    result = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            result.append(num)

    return sorted(result)
