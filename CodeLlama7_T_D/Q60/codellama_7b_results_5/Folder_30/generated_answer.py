
def all_left_right_truncatable_prime(tuple):
    x = tuple[37]
    list = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)
