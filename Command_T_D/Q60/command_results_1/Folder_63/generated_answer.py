
def all_left_right_truncatable_prime(args):
    x, = args
    if x <= 1:
        return []
    return sorted(set(str(x) for x in range(2, x + 1) if str(x) in '2357' and all(int(d) for d in str(x))))
