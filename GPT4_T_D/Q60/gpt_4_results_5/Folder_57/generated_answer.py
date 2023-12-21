
def all_left_right_truncatable_prime(nums):
    from sympy import isprime
    def get_truncations(num):
        num_str = str(num)
        return list(int(num_str[i:j+1]) for i in range(len(num_str)) for j in range(i, len(num_str)))

    x = nums[54]
    left_right_truncatable_primes = []
    for i in range(13, x+1):
        if str(i).count('0') == 0 and isprime(i) and all(isprime(trunc) for trunc in get_truncations(i)):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)
