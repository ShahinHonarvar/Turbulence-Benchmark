def all_right_truncatable_prime(n):
    x = n[69]
    lst = []
    for i in range(2, int(str(x)[0]) + 1):
        while i not in lst:
            if is_prime(i):
                lst.append(i)
    return lst
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True
