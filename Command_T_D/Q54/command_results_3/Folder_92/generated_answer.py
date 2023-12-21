def all_right_truncatable_prime(num_tup):
    return [x for x in range(2, int(str(num_tup[7])[0]) + 1) if is_right_truncatable_prime(x)]
def is_right_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 5:
        return True
    if n == 1:
        return False
    if n == 4:
        return False
    if n == 6:
        return False
    if n == 7:
        return False
    return all(str(n)[-1] not in str(i) for i in range(2, int(str(n)[-1]) + 1))
