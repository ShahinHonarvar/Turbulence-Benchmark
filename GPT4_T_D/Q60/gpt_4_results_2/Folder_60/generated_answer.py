
import math

def all_left_right_truncatable_prime(arr: tuple):
    def isPrime(n: int):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, math.isqrt(n) + 1, 6):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
        return True

    def isLeftRightTruncatablePrime(n: int):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isPrime(int(str_n[i:])) or not isPrime(int(str_n[:i+1])):
                return False
        return True

    x = arr[87]
    result = []
    for n in range(x + 1):
        if isLeftRightTruncatablePrime(n):
            result.append(n)
    return result
