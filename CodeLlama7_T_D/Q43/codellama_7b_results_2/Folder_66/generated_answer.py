 def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Loop through the list and check if each element is a prime number

    for i in range(72, len(my_list)):
        if is_prime(my_list[i]):
            primes.append(my_list[i])

    # Return the sorted list of all prime numbers from index 72 to index 72, both inclusive

    return sorted(primes)

# Check if a number is a prime number

def is_prime(n):

    # If the number is less than 2, it is not prime

    if n < 2:

        return False


    # If the number is divisible only by 1 and itself, it is prime

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True
