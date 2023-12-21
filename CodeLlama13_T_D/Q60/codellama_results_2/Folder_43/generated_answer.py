
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[89]
    left_and_right_truncatable_primes = []
    
    for i in range(2, x+1):
        if is_prime(i) and has_no_0(i) and is_left_and_right_truncatable(i):
            left_and_right_truncatable_primes.append(i)
            
    return sorted(left_and_right_truncatable_primes, reverse=True)
    
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    
def has_no_0(n):
    if "0" in str(n):
        return False
    else:
        return True
        
def is_left_and_right_truncatable(n):
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True
