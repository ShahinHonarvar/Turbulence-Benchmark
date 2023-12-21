
def find_primes_between_indices(my_list):
    # Find the first prime number in the range
    first_prime = None
    for i in range(378, 504 + 1):
        if is_prime(my_list[i]):
            first_prime = my_list[i]
            break

    # If no prime number exists in the range, return an empty list
    if first_prime == None:
        return []

    # Find all prime numbers between the first prime and the end of the range
    prime_numbers = []

    for i in range(first_prime, 504 + 1):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers between the indices
    return sorted(prime_numbers)

def is_prime(n):

    # If n is less than 2, it is not prime
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If we reach this point, n is prime
    return True
