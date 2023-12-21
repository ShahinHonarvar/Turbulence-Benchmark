
def all_left_right_truncatable_prime(args):
    return sorted(list(filter(lambda x: is_left_right_truncatable_prime(int(str(x)))), range(min(args), max(args)))))

def is_left_right_truncatable_prime(x):
    for i in range(2, len(str(x)) + 1):
        x //= 10**i
    return x > 1
