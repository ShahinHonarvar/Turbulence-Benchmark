
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(10, x+1):
        if is_left_and_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 10 or str(n).count('0') > 0:
        return False
    for i in range(len(str(n))-1, 0, -1):
        if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[i:])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
