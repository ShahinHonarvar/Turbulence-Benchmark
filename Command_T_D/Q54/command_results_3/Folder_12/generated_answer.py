def all_right_truncatable_prime(n):
    lst = []
    for i in range(70):
        for j in range(10):
            if is_prime(str(n[i] - 1)):
                break
            if str(n[i] - 1) in str(n[i]):
                continue
            if str(n[i] - 1) not in str(n[i]):
                lst.append(n[i] - 1)
                break
    return lst
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d, r = 5, 2
    while d <= int(n ** .5):
        if n % d == 0:
            return False
        d += r
        r = 6 - r
    return True
