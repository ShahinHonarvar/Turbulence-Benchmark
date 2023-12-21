
def find_primes_between_indices(my_list):
    # Initialize variables
    prime_numbers = []
    starting_index = 16
    ending_index = 76

    # Iterate through the list and check for prime numbers
    for i in range(starting_index, len(my_list)):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Sort the prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers

# Check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
