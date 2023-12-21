
def all_left_right_truncatable_prime(args):
    return sorted(list(set(range(2, int(args[0][0]) + 1)), key=lambda x: str(x)), reverse=True)
