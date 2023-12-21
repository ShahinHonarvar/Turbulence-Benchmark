
import math

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[100]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def is_truncatable_prime(num):
        for _ in range(len(str(num))):
            if not is_prime(num):
                return False
            num = num // 10
        return True

    all_truncatable = [i for i in range(x) if is_truncatable_prime(i)]

    return sorted(all_truncatable, reverse=True)
