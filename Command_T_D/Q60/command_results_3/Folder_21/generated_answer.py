
import math

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[175]
    y = x - 1
    while y > 0:
        y = int(str(y))
        if math.gcd(y, x) == 1:
            if is_left_and_right_truncatable_prime(y):
                yield y
            else:
                break
        y = y - 1
    for x in range(2, x + 1):
        if math.gcd(x, x_tuple[0]) == 1:
            if is_left_and_right_truncatable_prime(x):
                yield x
            else:
                break

def is_left_and_right_truncatable_prime(x):
    for y in range(2, int(str(x)[-2]) + 1):
        if x % 10 * 10 == x:
            return False
        elif x % 10 == 0:
            return False
        elif x % 10 == y:
            return False
        elif x % 10 == 9 and y == 2:
            return False
        elif x % 10 == 9 and y == 5:
            return False
        elif x % 10 == 8 and y == 2:
            return False
        elif x % 10 == 8 and y == 5:
            return False
        elif x % 10 == 7 and y == 2:
            return False
        elif x % 10 == 7 and y == 5:
            return False
        elif x % 10 == 6 and y == 2:
            return False
        elif x % 10 == 6 and y == 5:
            return False
        elif x % 10 == 5 and y == 2:
            return False
        elif x % 10 == 5 and y == 5:
            return False
        elif x % 10 == 4 and y == 2:
            return False
        elif x % 10 == 4 and y == 5:
            return False
        elif x % 10 == 3 and y == 2:
            return False
        elif x % 10 == 3 and y == 5:
            return False
        elif x % 10 == 2 and y == 2:
            return False
        elif x % 10 == 2 and y == 5:
            return False
        elif x % 10 == 1 and y == 2:
            return False
        elif x % 10 == 1 and y == 5:
            return False
    return True
