import re
def all_right_truncatable_prime(x_tup):
    x = x_tup[0]
    return sorted((p for p in range(2, x + 1) if all(p % d == 0 or p % d == d for d in range(2, int(str(p)[-1])))), reverse=True)
