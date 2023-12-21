
def all_left_truncatable_prime(x):
    result = []
    for i in range(10, x+1):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(1, int(len(str(n))/2)):
        if not is_prime(n/(10**i)):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
