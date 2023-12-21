
def all_left_right_truncatable_prime(l):
    return [p for p in l if p in l and p in range(l[0], l[-1] + 1) and l[0] > 1 and l[-1] > 1 and is_left_right_truncatable_prime(p)]

def is_left_right_truncatable_prime(n):
    if not (n >= 10):
        return False
    if n < 100:
        return True
    for i in range(2, int(str(n)[0]) + 1):
        if str(n)[i - 1] != '9':
            continue
        for j in range(2, int(str(n)[-1]) + 1):
            if str(n)[-j - 1] != '0':
                continue
            return False
    return True
