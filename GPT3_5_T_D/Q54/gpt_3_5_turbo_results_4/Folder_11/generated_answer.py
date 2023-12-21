
def all_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncatable_prime(num):
        num_str = str(num)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True

    x = nums[86]
    right_trunc_primes = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            right_trunc_primes.append(i)
    return sorted(right_trunc_primes)
