def all_left_truncatable_prime(x_tup):
    return sorted(set(x_tup[0] for x_tup[0] in range(2, x_tup[3] + 1) if all(x_tup[1](z) for z in range(x_tup[0], x_tup[0] + 10, 1) if x_tup[2](z)), reverse=True))
