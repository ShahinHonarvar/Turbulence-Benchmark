
def all_right_truncatable_prime(x):
    prime_list = []
    for i in range(10, x):
        if is_prime(i) and all([is_prime(i // 10 ** j) for j in range(1, len(str(i)))]):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
