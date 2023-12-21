
def all_left_truncatable_prime(tuple):
    x = tuple[77]
    list = []
    for i in range(2, x):
        if is_prime(i) and left_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)
