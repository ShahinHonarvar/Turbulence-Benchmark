def all_left_truncatable_prime(n):
    lst = []
    for i in range(2, n[0]):
        s = str(i)
        if s[0] != '0':
            while s:
                s = int(s[1:])
                if isprime(s):
                    lst.append(s)
    return lst
def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
