
def all_left_right_truncatable_prime(x):
    return sorted(list(filter(
        lambda n: is_left_right_truncatable_prime(n),
        range(2, x + 1)
    )), reverse=True)

def is_left_right_truncatable_prime(n):
    return all(n % 10**i != 0 for i in range(1, int(n ** .5) + 1))
