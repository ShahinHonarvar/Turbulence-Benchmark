
def all_left_truncatable_prime(tuple):
    x = tuple[78]
    list = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i, x)):
            list.append(i)
    return sorted(list, reverse=True)
