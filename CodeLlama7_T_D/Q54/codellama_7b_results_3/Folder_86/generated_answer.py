
def all_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[126]
    right_truncatable_primes = []
    
    # Iterate from 2 to x-1
    for i in range(2, x - 1):
        
        # Check if the number is prime
        if is_prime(i):
            
            # Check if the number is right-truncatable
            if is_right_truncatable(i):
                
                # Add the number to the list of right-truncatable prime numbers
                right_truncatable_primes.append(i)
    
    # Sort the list in descending order
    right_truncatable_primes.sort(reverse=True)
    
    # Return the sorted list of right-truncatable prime numbers less than x
    return right_truncatable_primes

def is_prime(n):
    """
    Check if a number is prime or not.
    """
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def is_right_truncatable(n):
    """
    Check if a number is right-truncatable or not.
    """
    if n < 2:
        return False
    
    while n > 0:
        if n % 10 == 0:
            return False
        
        n = int(n / 10)
    
    return True
