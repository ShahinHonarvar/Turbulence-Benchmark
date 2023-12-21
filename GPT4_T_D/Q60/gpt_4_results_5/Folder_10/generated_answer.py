
from sympy import isprime

def all_left_right_truncatable_prime(t):
    def check_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return n in [2, 3, 5, 7]
        elif '0' in str(n):
            return False
        else:
            num_str = str(n)
            for i in range(len(num_str)):
                if not check_prime(int(num_str[i:])) or not check_prime(int(num_str[:len(num_str) - i])):
                    return False
            return True

    x = t[38]
    primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes
