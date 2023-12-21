
def all_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[18]
    right_truncatable_primes = []
    
    # Loop through the numbers less than x
    for num in range(2, x + 1):
        
        # Check if the number is prime
        if is_prime(num):
            
            # Check if the number is right-truncatable prime
            if is_right_truncatable_prime(num):
                
                # Add the number to the list of right-truncatable prime numbers
                right_truncatable_primes.append(num)
    
    # Sort the list in descending order
    right_truncatable_primes.sort(reverse=True)
    
    # Return the sorted list
    return right_truncatable_primes

# Define a function to check if a number is prime
def is_prime(num):
    
    # Check if num is an integer greater than 1
    if not (isinstance(num, int) and num > 1):
        
        return False
    
    
    # Loop through the numbers less than or equal to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        
        # Check if i divides num
        if num % i == 0:
            
            return False
    
    
    # If the loop completes, then num is prime
    return True

# Define a function to check if a number is right-truncatable prime
def is_right_truncatable_prime(num):
    
    # Check if num is prime
    if not is_prime(num):
        
        return False
    
    
    # Loop through the numbers less than or equal to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        
        # Check if i divides num
        if num % i == 0:
            
            return False
    
    
    # If the loop completes, then num is right-truncatable prime
    return True
