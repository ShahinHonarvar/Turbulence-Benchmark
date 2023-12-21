
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple and check if each element is a prime number
    for i in range(len(tuple)):
        current_number = tuple[i]
        if is_prime(current_number):
            prime_numbers.append(current_number)

    # Sort the list of prime numbers in descending order
    sorted_prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the sorted list of right-truncatable prime numbers less than x
    return sorted_prime_numbers

# Function to check if a number is a prime number
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
