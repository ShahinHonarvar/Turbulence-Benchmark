
def all_left_right_truncatable_prime(n):
    x = int(n[0])
    return sorted(list(set(str(x)) + str(x)[1:-1]), reverse=True)
