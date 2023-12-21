
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers up to x
    primes = [i for i in range(2, x+1) if is_prime(i)]
    
    # create a list of left-and-right-truncatable prime numbers
    lrtp = []
    for p in primes:
        if is_left_right_truncatable_prime(p):
            lrtp.append(p)
    
    return sorted(lrtp, reverse=True)

def is_prime(n):
    # check if n is a prime number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    # check if n is a left-and-right-truncatable prime number
    if str(n).count('0') > 0:
        return False
    
    for i in range(1, len(str(n)) // 2 + 1):
        if not is_prime(int(str(n)[:len(str(n)) - i])) or not is_prime(int(str(n)[i:])):
            return False
    
    return True
