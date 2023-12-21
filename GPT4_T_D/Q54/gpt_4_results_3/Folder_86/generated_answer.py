
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[126]
    result = []

    for num in range(2, x):
        flag = True
        for i in range(len(str(num))):
            if not isprime(int(str(num)[0:i + 1])):
                flag = False
                break
        if flag:
            result.append(num)

    return sorted(result, reverse=True)
