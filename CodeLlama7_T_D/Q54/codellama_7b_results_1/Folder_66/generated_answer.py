
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple and check if each element is a prime number
    for i in range(len(tuple)):
        element = tuple[i]
        if is_prime(element) == True:
            prime_numbers.append(element)

    # Sort the list of prime numbers in descending order
    sorted_list = sorted(prime_numbers, reverse=True)

    return sorted_list

def is_prime(n):

    # Check if n is less than 2, if so it is not a prime number
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If none of the above conditions are true, it is a prime number
    return True
