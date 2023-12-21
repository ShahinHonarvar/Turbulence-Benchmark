
def all_left_right_truncatable_prime(tup):
    x = tup[77]
    return sorted(set(str(i) for i in range(2, x // 2 + 1) if all(int(d) for d in str(i)) and i % 2 == 1))
