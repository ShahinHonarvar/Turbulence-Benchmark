
def all_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    if len(nums) < 24:
        return []

    x = nums[23]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes)
