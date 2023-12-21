 def find_primes_between_indices(my_list):
    # Initialize a variable to store the prime numbers
    primes = []
    # Loop through the list of integers, starting from index 70
    for i in range(70, len(my_list)):
        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(math.sqrt(my_list[i])) + 1)):
            if my_list[i] % j == 0:
                # If the current element is divisible by any number between 2 and the square root of the current element, it is not prime
                break

        else:

            # If the current element is not divisible by any number between 2 and the square root of the current element, it is prime
            primes.append(my_list[i])
    # Sort the list of prime numbers in descending order
    primes.sort(reverse=True)
    # Return the sorted list of prime numbers
    return primes
