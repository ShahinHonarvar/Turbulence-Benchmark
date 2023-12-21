
import itertools

def all_left_right_truncatable_prime(x):
    all_left_right_truncatable_prime = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            all_left_right_truncatable_prime.append(i)
    return sorted(all_left_right_truncatable_prime)

def is_left_right_truncatable_prime(n):
    if n < 2 or n == 2 or n == 3:
        return True
    if n == 1:
        return False
    if str(n) == '0' or str(n) == '00':
        return False
    if str(n) == '1' or str(n) == '11':
        return True
    for i in range(2, len(str(n)) + 1):
        if str(n)[-i-1] != '0' and str(n)[i-1] != '0':
            continue
        elif str(n)[-i-1] == '0' and str(n)[i-1] == '0':
            return False
        elif str(n)[-i-1] == '0' and str(n)[i-1] == '1':
            return True
        elif str(n)[-i-1] == '1' and str(n)[i-1] == '0':
            return False
        elif str(n)[-i-1] == '1' and str(n)[i-1] == '1':
            return True
        else:
            return False
