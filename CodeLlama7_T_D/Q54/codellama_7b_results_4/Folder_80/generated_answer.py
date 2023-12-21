
def all_right_truncatable_prime(tuple_of_ints):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through each integer in the tuple
    for i in range(len(tuple_of_ints)):
        # Set x equal to the current integer in the tuple
        x = tuple_of_ints[i]

        # Check if x is a prime number and add it to the list if it is
        if is_prime(x):
            prime_numbers.append(x)

        # If x is not a prime number, check if it is a right-truncatable prime number and add it to the list if it is
        else:
            for j in range(len(str(x))) - 1):
                y = int(str(x)[:j] + str(x)[j + 1:]))
                if is_prime(y):
                    prime_numbers.append(y)

        # If the list of prime numbers is not empty, sort it in descending order and return it
        if len(prime_numbers) > 0:
            prime_numbers = sorted(prime_numbers, reverse=True))
            return prime_numbers

    # If the list of prime numbers is empty, return an empty list
    else:
        return []

# Function to check if a number is a prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
