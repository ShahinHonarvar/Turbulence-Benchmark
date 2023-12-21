
def all_left_right_truncatable_prime(x):
    # Create a list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers
```
Here is a possible implementation of the `is_prime` function:
```
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:

        # Return False since n is not a prime number
        return False

    # Check if n is divisible by 2, 3, 5, or 7
    for i in range(2, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    # Return True since n is a prime number
    return True
```
Here is a possible implementation of the `is_left_right_truncatable_prime` function:
```
def is_left_right_truncatable_prime(n):

    # Check if n contains any 0 digits
    if '0' in str(n):

        # Return False since n contains a 0 digit
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, int(n ** 0.5) + 1):

        # Check if the leading leftmost digit of n is divisible by i
        if str(n)[0] % i == 0:

            # Check if the last rightmost digit of n is divisible by i
            if str(n)[-1] % i == 0:

                # Remove the leading leftmost and last rightmost digits of n simultaneously successively
                temp = str(n)
                temp = temp[1:-1]

                # Check if the remaining digits of n are all prime numbers
                for j in range(1, int(temp ** 0.5) + 1):
                    if temp % j == 0:
                        return False

    # Return True since n is a left-and-right-truncatable prime number
    return True
