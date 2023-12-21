
def all_right_truncatable_prime(tuple):
    x = tuple[4]
    prime_numbers = []



    
    for i in range(2, x + 1):
        
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    
    return sorted(prime_numbers)



def is_prime(n):

    for i in range(2, int(math.sqrt(n)) + 1):
        
        if n % i == 0:
            return False

    return True



def is_right_truncatable_prime(n):

    
    while n > 0:
        
        if not is_prime(n):
            return False
        
        n = int(str(n)[:-1]))
    
    return True
