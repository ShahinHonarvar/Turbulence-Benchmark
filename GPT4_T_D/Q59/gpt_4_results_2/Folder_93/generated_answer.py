
def all_left_truncatable_prime(tup):
    from sympy import isprime
    x = tup[11]
    res = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str or not isprime(num):
            continue
        else:
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])):
                    break
            else: 
                res.append(num)
    return sorted(res)
