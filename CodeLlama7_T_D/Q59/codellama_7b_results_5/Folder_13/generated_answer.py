
def all_left_truncatable_prime(tuple):
    x = tuple[784]
    list = []
    for i in range(2, x):
        if is_prime(i) and left_truncate(i) == True:
            list.append(i)
    return sorted(list)
