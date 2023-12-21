
def all_left_right_truncatable_prime(n):
    n = str(n)
    res = []
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] != '0' and n[j] != '0':
                if len(n) > 2:
                    n = n[1:-1]
                else:
                    n = '1'
                if isprime(int(n)):
                    res.append(int(n))
    return res
