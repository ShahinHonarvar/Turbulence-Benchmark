
import sys

def all_left_right_truncatable_prime(x):
    def is_left_right_truncatable(n):
        i = j = 0
        while j < len(str(n)):
            j += 1
            if str(n)[j-1] == '0':
                return False
            if str(n)[i] == '0':
                return False
            i += 1
        return True

    res = []
    for n in range(2, x + 1):
        if is_left_right_truncatable(n) and all(n % i == 0 for i in range(3, int(str(n)[-1]))) and n != 1:
            res.append(n)
    return res
