
def all_left_right_truncatable_prime(nums):
    import sympy

    def is_prime(n):
        return sympy.isprime(n)

    def truncatable_prime(x):
        str_x = str(x)
        if '0' in str_x:
            return False
        for i in range(len(str_x)):
            left_x = int(str_x[i:])
            right_x = int(str_x[:len(str_x) - i])
            if not is_prime(left_x) or not is_prime(right_x):
                return False
        return True

    x = nums[100]
    truncatable_primes = []
    for num in range(10, x + 1):
        if truncatable_prime(num):
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
