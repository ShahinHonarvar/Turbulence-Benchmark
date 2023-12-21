def all_left_truncatable_prime(x_tuple):
    x = x_tuple[77]
    return sorted(set(str(x) for x in range(2, x + 1) if all(int(d) for d in str(x - 1)))), reverse=True)
