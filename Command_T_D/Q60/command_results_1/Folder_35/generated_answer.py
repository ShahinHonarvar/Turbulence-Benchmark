
import sys

input = sys.stdin.readline

def all_left_right_truncatable_prime(test_tup):
    test_num = test_tup[177]
    primes = []
    for x in range(2, test_num + 1):
        if all(d not in str(x) for d in "0"):
            break
        if x * 10 * 10 <= test_num:
            if all(str(x)[:i] not in str(x) for i in range(1, len(str(x)))):
                break
            if all(str(x)[-i:] not in str(x) for i in range(1, len(str(x)))):
                break
        elif x * 10 <= test_num:
            if all(str(x)[:i] not in str(x) for i in range(1, len(str(x)))):
                break
        elif x <= test_num:
            if all(str(x)[-i:] not in str(x) for i in range(1, len(str(x)))):
                break
        else:
            continue
        primes.append(x)
    return primes
