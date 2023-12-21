
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:i+1])):
                return False
        return True

    x = nums[98]
    truncatable_primes = []
    for i in range(11, x+1):
        if '0' not in str(i) and is_truncatable(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes)
