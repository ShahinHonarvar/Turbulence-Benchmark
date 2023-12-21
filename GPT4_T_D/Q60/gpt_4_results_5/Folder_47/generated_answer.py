
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            left = int(str_n[i:])
            right = int(str_n[:length - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = nums[49]
    primes = []
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)
