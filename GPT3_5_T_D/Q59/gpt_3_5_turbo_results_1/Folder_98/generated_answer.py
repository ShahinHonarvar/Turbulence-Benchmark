
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[8]
    truncatable_primes = []
    for i in range(10, x):
        if is_prime(i):
            num_str = str(i)
            is_truncatable = True
            for j in range(len(num_str) - 1):
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
