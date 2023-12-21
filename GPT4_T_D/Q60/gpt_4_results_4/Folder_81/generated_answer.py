
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        len_n = len(str_n)
        for i in range(len_n):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len_n - i])):
                return False
        return True

    x = nums[98]
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
