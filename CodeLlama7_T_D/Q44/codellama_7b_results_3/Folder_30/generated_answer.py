
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list and check if each number is composite
    for i, num in enumerate(my_list):
        # If the number is not prime, add it to the set of composite numbers
        if i >= 19 and i <= 92 and not num_is_prime(num):
            composite_nums.add(num)
    return composite_nums

# Check if a number is prime using the Sieve of Eratosthenes algorithm
def num_is_prime(n):
    # If the number is less than 2, it is not prime
    if n < 2:
        return False

    # Mark numbers up to the square root of n as composite
    sieve = [True] * (n + 1)
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    # Return True if the number is prime and False otherwise
    return sieve[n]
