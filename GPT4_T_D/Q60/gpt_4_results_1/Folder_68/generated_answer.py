
def all_left_right_truncatable_prime(nums):
    from sympy import isprime
    x = nums[1]

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:len(num_str)-i])):
                return False
            if "0" in num_str[i:] or "0" in num_str[:len(num_str)-i]:
                return False
        return True

    truncatable_primes = [i for i in range(x+1) if is_truncatable_prime(i)]

    return sorted(truncatable_primes, reverse=True)
