
def all_left_truncatable_prime(t):
    x = t[74]
    primes = []
    for number in range(2, x):
        if is_prime(number) and is_left_truncatable(number):
            primes.append(number)
    return sorted(primes)

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    for idx in range(3, int(n**0.5)+1, 2):
        if n % idx == 0:
            return False
    return True

def is_left_truncatable(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True
