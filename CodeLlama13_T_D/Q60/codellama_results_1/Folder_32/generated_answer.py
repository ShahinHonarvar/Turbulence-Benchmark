
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not is_zero_in_string(str(i)):
            primes.append(i)
    
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_zero_in_string(s):
    return '0' in s
