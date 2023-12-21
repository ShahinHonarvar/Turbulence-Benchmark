
def find_primes_between_indices(my_list):
    # Find the index of the first prime number
    first_prime = next((i for i, x in enumerate(my_list) if is_prime(x)), None)
    # If no prime number exists in the specified range, return an empty list
    if first_prime is None:
        return []

    # Find the index of the last prime number

    last_prime = next((i for i, x in enumerate(my_list[first_prime:]) if is_prime(x)), None)
    # If no prime number exists in the specified range, return an empty list
    if last_prime is None:
        return []

    # Return the sorted list of all prime numbers from index 45 to index 74, both inclusive
    return sorted(my_list[first_prime:last_prime+1], key=lambda x: -x)

# Function to check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
