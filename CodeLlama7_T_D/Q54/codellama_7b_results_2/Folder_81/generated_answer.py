
def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 10 to x-1
    for i in range(10, x):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is right-truncatable
            if is_right_truncatable(i):

                # Add the prime number to the list
                prime_list.append(i)

    # Sort the list in ascending order
    prime_list.sort()

    # Return the sorted list of prime numbers
    return prime_list

# Check if a number is prime
def is_prime(n):

    # Check if n is less than 2
    if n < 2:

        # If yes, then it is not a prime number
        return False

    # Check if n is divisible by any number between 2 and sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):

        # If yes, then it is not a prime number
        if n % i == 0:

            return False

    # If no, then it is a prime number
    return True

# Check if a number is right-truncatable
def is_right_truncatable(n):

    # Initialize the result to True
    result = True

    # Check if n is less than 10
    if n < 10:

        # If yes, then it is not right-truncatable
        return False

    # Check if the last digit of n is not 0 or 5
    if int(str(n)[-1]) in [0, 5]:

        # If yes, then it is not right-truncatable
        return False

    # Check if the number remains prime when the last rightmost digit is successively removed
    while n > 9:

        # Check if the number is not prime
        if not is_prime(n):

            # If yes, then it is not right-truncatable
            return False

        # Remove the last rightmost digit of n
        n = int(str(n)[:-1])

    # Return the result of the check
    return result
