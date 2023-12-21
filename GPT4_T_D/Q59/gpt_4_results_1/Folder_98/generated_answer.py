
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    
def all_left_truncatable_prime(t):
    x = t[8]
    lt_primes = []
    for i in range(2, x):
        if "0" in str(i):
            continue
        str_i = str(i)
        for j in range(len(str_i)):
            if not is_prime(int(str_i[j:])):
                break
        else:
            lt_primes.append(i)
    lt_primes.sort(reverse=True)
    return lt_primes
