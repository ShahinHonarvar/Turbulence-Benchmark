
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Iterate through the tuple and check if each element is a prime number
    for i in range(len(tuple)):
        if is_prime(tuple[i]):
            # If the element is a prime number, add it to the list of prime numbers
            prime_list.append(tuple[i])

    # Sort the list of prime numbers in descending order
    prime_list = sorted(prime_list, reverse=True)

    # Return the list of prime numbers
    return prime_list

# Check if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of those numbers
def is_prime(n):
    # If the number is less than 2, it is not prime
    if n < 2:
        return False

    # Iterate from 2 to the square root of the number and check if the number is divisible by any of those numbers
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by any of the numbers from 2 to the square root of the number, then it is prime
    return True
