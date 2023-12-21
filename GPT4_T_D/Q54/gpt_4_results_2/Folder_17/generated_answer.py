
def all_right_truncatable_prime(nums):
    from sympy import isprime

    def is_right_truncatable_prime(num):
        while isprime(num):
            num //= 10
            if num == 0:
                return True
        return False

    x = nums[36]
    right_truncatable_primes = []

    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
