
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[433]
    right_truncatables = []
    for num in range(x - 1, 10, -1):
        temp = num
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            right_truncatables.append(num)
    return sorted(right_truncatables, reverse=True)
