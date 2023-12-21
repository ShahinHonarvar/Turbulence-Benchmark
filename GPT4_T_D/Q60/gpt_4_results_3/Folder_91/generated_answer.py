
from math import sqrt

def all_left_right_truncatable_prime(numbers):
    prime_nums = []

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    for num in range(numbers[0], 1, -1):
        if is_truncatable_prime(num):
            prime_nums.append(num)

    return sorted(prime_nums, reverse=True)
