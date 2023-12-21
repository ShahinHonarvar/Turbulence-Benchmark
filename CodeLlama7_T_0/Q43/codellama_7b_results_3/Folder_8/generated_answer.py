
def find_primes_between_indices(my_list):
    # Find the first prime number in the range
    first_prime = None
    for i in range(43, 76 + 1):
        if is_prime(my_list[i]):
            first_prime = my_list[i]
            break

    # Find all prime numbers in the range

    prime_numbers = []

    for i in range(43, 76 + 1):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order

    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers

    return prime_numbers


def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True
