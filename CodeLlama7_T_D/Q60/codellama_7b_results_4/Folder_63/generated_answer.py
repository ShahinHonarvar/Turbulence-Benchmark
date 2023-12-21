
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x (sorted in ascending order)
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the value of n % 2
        remainder = n % 2

        # Check if the remainder is equal to 0
        if remainder == 0:
            # Return False (n is not prime)
            return False

        # Check if the remainder is equal to 1
        elif remainder == 1:
            # Initialize a variable to store the value of n - 1
            decremented_n = n - 1

            # While the value of decremented_n is greater than 1
            while decremented_n > 1:
                # Check if the remainder of decremented_n divided by 2 is equal to 0
                if decremented_n % 2 == 0:
                    # Return False (decremented_n is not prime)
                    return False

                # Decrement decremented_n by 1
                decremented_n -= 1

        # Return True (n is prime)
        return True

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False (n is not a prime number)
        return False

    # Initialize variables to store the values of n / 10 and n % 10
    quotient = n // 10
    remainder = n % 10

    # Check if the remainder is equal to 0
    if remainder == 0:
        # Return False (n is not a left-and-right-truncatable prime number)
        return False

    # While the value of quotient is greater than or equal to 1
    while quotient >= 1:
        # Check if the remainder of quotient divided by 2 is equal to 0
        if quotient % 2 == 0:
            # Return False (quotient is not a prime number)
            return False

        # Decrement quotient by 1
        quotient -= 1

    # Return True (n is a left-and-right-truncatable prime number)
    return True

# Test the 'all_left_right_truncatable_prime' function with different inputs
#print(all_left_right_truncatable_prime((10, 20, 30)))) # Output: [23]
#print(all_left_right_truncatable_prime((10, 20, 30, 40)))) # Output: [23, 37]
#print(all_left_right_truncatable_prime((10, 20, 30, 40, 50)))) # Output: [23, 37, 53]

# Function to check if a number is a strong pseudo-prime number
def is_strong_pseudoprime(n):
    # Initialize variable 'count' to store the number of digits in n
    count = len(str(n))

    # Check if the number of digits in n is equal to 3 or 4
    if count == 3 or count == 4:
        # While the value of decremented_n is greater than or equal to 1
        while n >= 1:
            # Initialize variables 'sum' and 'product' to store the sum and product of the digits in n
            sum = 0
            product = 1

            # While the value of decremented_n is greater than or equal to 1
            while n >= 1:
                # Check if the remainder of decremented_n divided by 2 is equal to 0
                if n % 2 == 0:
                    # Return False (n is not a strong pseudo-prime number)
                    return False

                # Increment sum by the value of decremented_n modulo 10
                sum += n % 10

                # Multiply product by the value of decremented_n modulo 10
                product *= n % 10

                # Decrement decremented_n by 1
                n -= 1

            # Check if sum and product are equal
            if sum == product:
                # Return True (n is a strong pseudo-prime number)
                return True

    # Return False (n is not a strong pseudo-prime number)
    return False

# Function to check if a number is an almost prime number
def is_almost_prime(n):
    # Initialize variable 'count' to store the number of digits in n
    count = len(str(n)))

    # Check if the number of digits in n is equal to 3 or 4
    if count == 3 or count == 4:
        # Initialize variable 'remainder' to store the remainder of dividing n by 10
        remainder = n % 10

        # Check if the value of remainder is equal to 1 or 3
        if remainder == 1 or remainder == 3:
            # Return True (n is an almost prime number)
            return True

    # Return False (n is not an almost prime number)
    return False

# Function to check if a number is an almost prime number that has been generated using the previous two functions 'is_strong_pseudoprime' and 'is_almost_prime'
def is_strong_almost_prime(n):
    # Check if n is an almost prime number
    if is_almost_prime(n) == True:
        # Check if n is a strong pseudo-prime number
        if is_strong_pseudoprime(n) == True:
            # Return True (n is a strong pseudo-prime and almost prime number)
            return True

    # Return False (n is not a strong pseudo-prime or almost prime number)
    return False

# Function to check if a number is a strong pseudo-prime that has been generated using the previous two functions 'is_strong_pseudoprime' and 'is_almost_prime'
def is_strong_pseudoprime(n):
    # Check if n is an almost prime number
    if is_almost_prime(n) == True:
        # Check if n is a strong pseudo-prime number
        if is_strong_pseudoprime(n) == True:
            # Return True (n is a strong pseudo-prime and almost prime number)
            return True

    # Return False (n is not a strong pseudo-prime or almost prime number)
    return False
