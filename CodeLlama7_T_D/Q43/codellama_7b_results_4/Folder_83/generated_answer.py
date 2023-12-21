
def find_primes_between_indices(my_list):
    # Find the first prime number in the range
    first_prime = None
    for i in range(14, len(my_list)):
        if is_prime(my_list[i]):
            first_prime = my_list[i]
            break

    # If no prime number exists in the specified range, return an empty list
    if first_prime == None:
        return []

    # Find all prime numbers between the first prime number and the last element of the list
    prime_numbers = []

    for i in range(first_prime, len(my_list)):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 14 to index 73, both inclusive, in descending order
    return sorted(prime_numbers, reverse=True)

def is_prime(n):

    # If n is less than or equal to 1, it is not a prime number
    if n <= 1:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the loop completes successfully, n is a prime number
    return True
