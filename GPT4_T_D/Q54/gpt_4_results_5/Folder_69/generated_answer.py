
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[:len(n_str)-i])):
                return False
        return True

    x = nums[760]
    rt_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            rt_primes.append(i)
    return sorted(rt_primes, reverse=True)
