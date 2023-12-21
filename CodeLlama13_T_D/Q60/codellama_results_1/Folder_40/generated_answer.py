
def all_left_right_truncatable_prime(x):
    x = tuple([int(i) for i in str(x)])
    prime_list = []
    for i in range(len(x)):
        if is_prime(x[i]):
            prime_list.append(x[i])
    return sorted(prime_list, reverse=True)
