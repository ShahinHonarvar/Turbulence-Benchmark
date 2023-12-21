
def all_left_right_truncatable_prime(n):
    i = 100
    while i < n[0]:
        i += 1
    j = n[0] - 1
    while j >= 2:
        j -= 1
    return sorted(n[0] - 1 for n in range(2, i) if all(n % d == 0 or n % d == d for d in range(2, n.bit_length() + 1)))
