
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    digits = str(n)
    for i in range(len(digits)):
        if int(digits[:i]) % 3 == 0 and int(digits[i:]) % 7 == 0:
            return True
    return False
