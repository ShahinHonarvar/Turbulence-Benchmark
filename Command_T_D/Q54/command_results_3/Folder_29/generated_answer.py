import sys
def all_right_truncatable_prime(n):
    x = n[55]
    return sorted(list(filter(lambda x: all(int(d) > 0 for d in str(x)), x + 1)), reverse=True)
