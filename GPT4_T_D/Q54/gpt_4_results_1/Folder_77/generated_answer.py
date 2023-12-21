
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[:len(str(n)) - i])):
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[767]
    res = []
    for num in range(1, x):
        if is_right_truncatable(num):
            res.append(num)
    res.sort(reverse=True)
    return res
