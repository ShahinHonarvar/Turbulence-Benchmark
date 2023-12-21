 def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    primes = []
    # Loop through the list of integers starting from index 38 and ending at index 94
    for i in range(38, 95):
        # Check if the current number is a prime number by dividing it by all the numbers less than or equal to its square root
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the current number is a prime number, add it to the list of prime numbers
        if is_prime:
            primes.append(i)

    # Return the sorted list of prime numbers in ascending order
    return sorted(primes)
