
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:length-i])):
                return False
        return True

    x = nums[78]
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
