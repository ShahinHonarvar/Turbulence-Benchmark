
def all_left_truncatable_prime(tuple):
    x = tuple[126]
    prime_list = []
    for i in range(x):
        if is_prime(i) and left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
