import math
def all_right_truncatable_prime(n):
    return [int(i) for i in range(2, int(math.ceil(str(n)[-1]))) if all(int(d) not in range(2, int(math.ceil(str(i)[-1]))) for d in str(i)[::-1])]
