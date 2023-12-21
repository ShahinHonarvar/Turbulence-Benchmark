
def all_right_truncatable_prime(nums):
    x = nums[24]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True

    def is_right_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True

    rt_primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            rt_primes.append(i)

    return sorted(rt_primes)
