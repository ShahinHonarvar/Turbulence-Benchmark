
def all_left_right_truncatable_prime(tup):
    return sorted(filter(lambda x: x.is_left_right_truncatable_prime(), map(str, range(2, int(tup[24]) + 1))))
