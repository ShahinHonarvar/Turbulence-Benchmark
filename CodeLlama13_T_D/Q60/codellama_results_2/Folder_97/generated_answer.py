
def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x+1):
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)

def is_left_and_right_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        n = int(str(n)[1:-1])
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
