
def all_right_truncatable_prime(tuple):
    # Initialize an empty list for storing results
    primeList = []
    # Extract the integer at index 22 from the tuple
    x = tuple[22]
    # Iterate over all prime numbers less than x
    for i in range(2,x):
        # Check if the current prime number is right-truncatable
        if is_right_truncatable_prime(i) == True:
            # If it is, add it to the list of prime numbers
            primeList.append(i)
    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(primeList,reverse=True)
