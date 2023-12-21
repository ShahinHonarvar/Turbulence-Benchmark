
def all_right_truncatable_prime(x):
    prime_list = []
    for i in range(10**53, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
