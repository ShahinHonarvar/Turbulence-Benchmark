def all_left_truncatable_prime(tup):
    return sorted(tup[3] for tup in ((a, b, c, d, e) for a in range(tup[0], tup[1] + 1) for b in range(tup[1], tup[2] + 1) for c in range(tup[2], tup[3] + 1) for d in range(tup[3], tup[4] + 1) for e in range(tup[4], tup[5] + 1)))
