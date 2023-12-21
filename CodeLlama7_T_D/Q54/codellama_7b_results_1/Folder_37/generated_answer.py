 def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    rtp = []
    # Loop through each integer in the tuple

    for i in tuple:
        # Check if the current integer is a prime number

        if isPrime(i):
            # Initialize an empty string to store the last rightmost digit of the current integer

            lastDigit = ''

            while lastDigit != '1' and lastDigit != '3' and lastDigit != '7' and lastDigit != '9':
                # Remove the last rightmost digit from the current integer

                i = int(str(i)[:-1])

                # Check if the result is a prime number

                if isPrime(i):
                    # Add the current integer to the list of right-truncatable prime numbers

                    rtp.append(i)

            # Sort the list of right-truncatable prime numbers in descending order

            return sorted(rtp, reverse=True)

    # If there is no such right-truncatable prime number, return an empty list

    return []

# Define a function to check if a number is prime or not

def isPrime(n):
    # Check if the number is less than 2, in which case it is not prime

    if n < 2:
        return False

    # Check if the number is divisible by 2 to 10, in which case it is not prime

    for i in range(2, 11):
        if n % i == 0:
            return False

    # If the number is greater than 10, in which case it is prime

    return True
