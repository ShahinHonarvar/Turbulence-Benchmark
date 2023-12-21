
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list and check if each element is a prime number
    for i in range(28, 45):
        if is_prime(i):
            prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is prime by dividing it by all the numbers less than or equal to its square root
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
