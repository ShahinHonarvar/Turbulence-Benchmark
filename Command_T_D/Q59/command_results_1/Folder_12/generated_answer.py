def all_left_truncatable_prime(n):
    return sorted(list(filter(left_truncatable_prime, range(n[0] - 1, n[1] + 1))), reverse=True)
def left_truncatable_prime(n):
    return not str(n).count("0") and str(n)[0] in "2357"
