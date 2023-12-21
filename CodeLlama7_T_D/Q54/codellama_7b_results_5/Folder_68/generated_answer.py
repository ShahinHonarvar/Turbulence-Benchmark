 def all_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[1]
    right_truncatable_prime_numbers = []
    
    # Iterate through numbers from 2 to x
    for i in range(2, x + 1):
        
        # Check if the number is prime
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the number is prime and right-truncatable prime, add it to the list
        if is_prime:
            right_truncatable_prime_numbers.append(i)

    # Sort the list in descending order and return it
    return sorted(right_truncatable_prime_numbers, reverse=True)
