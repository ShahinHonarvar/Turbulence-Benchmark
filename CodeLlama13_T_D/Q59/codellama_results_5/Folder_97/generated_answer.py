
def all_left_truncatable_prime(x):
    lst = []
    for i in range(10, x):
        if is_prime(i) and not contains_zero(str(i)):
            lst.append(i)
    return sorted(lst)
