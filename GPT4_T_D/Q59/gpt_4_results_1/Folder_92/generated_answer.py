
import sympy

def all_left_truncatable_prime(t):
    x = t[7]

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        return False

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return True

    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
