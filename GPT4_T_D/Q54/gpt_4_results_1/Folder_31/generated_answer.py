
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prim(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = nums[50]

    truncatable_primes = []
    for num in range(x):
        if is_right_truncatable_prim(num):
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
