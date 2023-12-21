
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[3]
    right_truncatable_primes = []
    
    for num in range(2, x+1):
        if is_prime(num) and all(is_right_truncatable_prime(num, i) for i in range(1, len(str(num)))):
            right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(num, i):
    while len(str(num)) > i:
        num = int(str(num)[:-i])
        if not is_prime(num):
            return False
    return True
