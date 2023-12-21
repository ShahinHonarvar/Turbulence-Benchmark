
def all_left_right_truncatable_prime(x):
    return sorted(x for x in range(2, x) if all(str(x).count(d) > 1 for d in str(x) if d!='0'))
