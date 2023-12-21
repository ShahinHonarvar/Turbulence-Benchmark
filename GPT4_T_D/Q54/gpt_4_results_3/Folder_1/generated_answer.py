
import math

def all_right_truncatable_prime(tuple):
    x = tuple[20]

    # check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True
      
    # check if a number is right_truncatable_prime
    def is_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True

    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)
