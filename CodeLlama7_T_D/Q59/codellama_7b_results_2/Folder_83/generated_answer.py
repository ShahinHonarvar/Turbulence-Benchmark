
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the left-truncatable prime numbers
    prime_list = []

    # Iterate through the tuple and check if each element is a prime number

    for i in range(len(tuple)):
        x = tuple[i]
        if is_prime(x):
            prime_list.append(x)

    # Sort the list of prime numbers in ascending order

    prime_list.sort()

    # Return the sorted list of left-truncatable prime numbers less than x

    return prime_list

# Check if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any other number between 2 and the square root of the number

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
