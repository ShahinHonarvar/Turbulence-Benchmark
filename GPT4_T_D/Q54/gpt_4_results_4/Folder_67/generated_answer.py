
def all_right_truncatable_prime(nums):
    from sympy import isprime

    def is_right_truncatable(n):
        strn = str(n)
        return all(isprime(int(strn[:i])) for i in range(len(strn), 0, -1))

    x = nums[71]
    primes = [i for i in range(x) if isprime(i) and is_right_truncatable(i)]
    primes.sort(reverse=True)
    return primes
