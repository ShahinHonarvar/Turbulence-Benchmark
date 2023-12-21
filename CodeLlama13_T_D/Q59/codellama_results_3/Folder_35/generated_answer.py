
def all_left_truncatable_prime(x):
    lst = []
    for i in range(1, x+1):
        if is_left_truncatable_prime(i):
            lst.append(i)
    return sorted(lst)
