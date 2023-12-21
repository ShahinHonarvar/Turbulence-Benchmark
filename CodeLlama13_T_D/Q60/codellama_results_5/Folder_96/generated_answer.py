
def all_left_right_truncatable_prime(x):
    lst = []
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            lst.append(i)
    return sorted(lst)

def is_left_right_truncatable_prime(n):
    if n < 2 or not is_prime(n):
        return False
    while n > 0:
        n = int(str(n)[1:-1])
        if not is_prime(n):
            return False
    return True

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
