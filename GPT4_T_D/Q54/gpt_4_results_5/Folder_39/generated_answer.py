
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[30]
    results = []
    for num in range(2, x):
        temp = num
        while isprime(temp) and temp > 0:
            temp = int(str(temp)[:-1])
            if temp == 0:
                results.append(num)
    return sorted(results, reverse=True)
