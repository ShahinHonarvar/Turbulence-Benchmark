
def all_left_truncatable_prime(mytuple):
    x = mytuple[78]
    lst = []
    for i in range(x):
        if is_prime(i) and not '0' in str(i):
            lst.append(i)
    return sorted(lst, reverse=True)
