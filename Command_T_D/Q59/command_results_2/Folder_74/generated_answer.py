def all_left_truncatable_prime(num_list):
    x = num_list[36]
    res = []
    for p in range(2, x // 2):
        if is_prime(p):
            q = str(p)
            while q:
                if q[0] != '0':
                    break
                q = q[1:]
            if q == '':
                res.append(p)
    return res
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**0.5
    i = 5
    while i <= maxDivisor:
        if n % i == 0:
            return False
        i += 6
    return True
