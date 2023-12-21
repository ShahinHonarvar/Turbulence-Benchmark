import itertools
def all_left_truncatable_prime(n):
    return sorted(list(filter(left_truncatable_prime, range(2, n[0] + 1))), reverse=True)
def left_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if str(n)[-i:] in '2357':
            break
    if n % 10 == 0:
        return True
    if str(n)[-i:] in '2357':
        return True
    for d in range(10, n // 10 + 1):
        if str(n - d)[-i:] in '2357':
            return True
    return False
