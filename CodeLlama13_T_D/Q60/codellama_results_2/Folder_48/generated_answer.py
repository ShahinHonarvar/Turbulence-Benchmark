
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_left_and_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_left_and_right_truncatable_prime(n):
    if n < 2 or str(n).count("0") > 0:
        return False
    for i in range(1, len(str(n))//2+1):
        left = int(str(n)[:i])
        right = int(str(n)[-i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
