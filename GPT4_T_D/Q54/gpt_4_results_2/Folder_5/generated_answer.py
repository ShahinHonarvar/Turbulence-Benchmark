
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    def is_right_truncatable(n):
        while isprime(n):
            n = int(str(n)[:-1])
            if n == 0:
                return True
        return False

    result = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(result)
