 def all_right_truncatable_prime(tuple_of_integers):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    
    # Iterate over the elements of the tuple
    for element in tuple_of_integers:
        
        # Check if the current element is a prime number
        if is_prime(element):
            
            # Add the current element to the list of prime numbers
            prime_numbers.append(element)

    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    
    # Check if n is greater than 1
    if n > 1:
        
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            
            # Check if i divides n
            if n % i == 0:
                
                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True
