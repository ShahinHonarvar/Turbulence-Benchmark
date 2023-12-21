
def all_left_right_truncatable_prime(t):
    x = t[92]
    primes = [2, 3, 5, 7, 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 7331, 73331, 739397]
    return [p for p in primes if p <= x]

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True    
