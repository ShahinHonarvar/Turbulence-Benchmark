
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    def is_left_right_truncatable_prime(n):
        if n < 10:
            return isprime(n)
        else:
            if "0" in str(n):
                return False
            else:
                return isprime(n) and is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))

    x = numbers[29]
    res = [i for i in range(10, x+1) if is_left_right_truncatable_prime(i)]
    res.sort(reverse=True)

    return res
