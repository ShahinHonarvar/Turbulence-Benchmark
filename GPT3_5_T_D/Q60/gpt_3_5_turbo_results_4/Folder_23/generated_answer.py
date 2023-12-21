
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    if not is_prime(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(arr):
    x = arr[77]
    res = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            res.append(i)
    return sorted(res, reverse=True)
