def all_left_truncatable_prime(n):
    a, b, c, d = n[2], n[4], n[6], n[8]
    l = [str(a), str(b), str(c), str(d)]
    return [int(i) for i in sorted(l, reverse=True) if all(int(i) for i in str(int(i)) if i != '0' and i != '1' and int(i) > 1)]
