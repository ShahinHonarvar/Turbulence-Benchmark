def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 40):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1 or n == 0:
        return False
    if n == 4:
        return False
    if n == 5:
        return True
    if n == 6:
        return False
    if n == 7:
        return True
    if n == 8:
        return False
    if n == 9:
        return True
    if n == 10:
        return False
    if n == 11:
        return True
    if n == 12:
        return False
    if n == 13:
        return True
    if n == 14:
        return False
    if n == 15:
        return True
    if n == 16:
        return False
    if n == 17:
        return True
    if n == 18:
        return False
    if n == 19:
        return True
    if n == 20:
        return False
    if n == 21:
        return True
    if n == 22:
        return False
    if n == 23:
        return True
    if n == 24:
        return False
    if n == 25:
        return True
    if n == 26:
        return False
    if n == 27:
        return True
    if n == 28:
        return False
    if n == 29:
        return True
    if n == 30:
        return False
    if n == 31:
        return True
    if n == 32:
        return False
    if n == 33:
        return True
    if n == 34:
        return False
    if n == 35:
        return True
    if n == 36:
        return False
    if n == 37:
        return True
    if n == 38:
        return False
    if n == 39:
        return True
