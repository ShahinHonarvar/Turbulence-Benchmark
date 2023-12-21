
def all_right_truncatable_prime(x):
    x = sorted(set([int(''.join(str(x)[::-1][i:])) for i in range(len(str(x)))]))
    return [i for i in x if is_prime(i) and all(is_prime(i//10**k) for k in range(1, len(str(x))))]
