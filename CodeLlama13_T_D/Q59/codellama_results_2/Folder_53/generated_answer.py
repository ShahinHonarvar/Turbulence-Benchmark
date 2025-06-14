
def all_left_truncatable_prime(tuple_of_positive_integers):
    return sorted([x for x in tuple_of_positive_integers if is_left_truncatable_prime(x)], reverse=True)

def is_left_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False
    
    # Check if n contains any 0s
    if '0' in str(n):
        return False
    
    # Check if the leading leftmost digit is removed and the result is still a prime number
    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    
    # If all conditions are met, n is a left-truncatable prime number
    return True

def is_prime(n):
    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If n is not divisible by any number between 2 and the square root of n, it is prime
    return True
