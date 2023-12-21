
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers and check if each number is composite
    for i in range(len(my_list)):
        # If the current number is not prime, add it to the set of composite numbers
        if not is_prime(my_list[i]):
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 0 to index 6, both inclusive
    return composite_numbers

# Check if a number is prime using the Sieve of Eratosthenes algorithm
def is_prime(n):
    # If the number is less than 2, it is not prime
    if n < 2:
        return False

    # Create a boolean array where each index corresponds to a number and the value is True if the number is prime and False otherwise
    sieve = [True] * (n + 1)

    # Iterate over the indices of the boolean array starting from 2 and multiplying by all numbers less than or equal to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            # Mark as composite all numbers that are multiples of i greater than i^2
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Return True if the number is prime and False otherwise
    return sieve[n]
