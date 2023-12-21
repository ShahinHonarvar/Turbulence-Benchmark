
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        digits = list(str(n))
        if '0' in digits:
            return False
        for i in range(len(digits)):
            left = int(''.join(digits[i:]))
            right = int(''.join(digits[:len(digits) - i]))
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = nums[7]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)

    return truncatable_primes
