
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through all possible prime numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if isprime(i):
            # Initialize an empty string to store the representation of i
            i_string = ""

            # Append the digits of i to i_string from left to right
            for digit in str(i):
                i_string += digit

            # Check if i_string is a left-and-right-truncatable prime number
            if isleft_right_truncatable_prime(i_string):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers, reverse=True)
```
Here is a possible implementation of the `isleft_right_truncatable_prime` function in :
```
def isleft_right_truncatable_prime(i):
    # Check if i is a prime number
    if isprime(i):
        # Initialize an empty string to store the representation of i
        i_string = ""

        # Append the digits of i to i_string from left to right
        for digit in str(i):
            i_string += digit

        # Check if i_string contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
        if "0" not in i_string and isprime(int(i_string[1:])) and isprime(int(i_string[:-1])):
            # Return True if i_string contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
            return True

    # Return False if i is not a prime number or if i_string contains 0 or does not remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    return False
```
Here is a possible implementation of the `isprime` function in :
```
def isprime(n):
    # Check if n is an integer greater than 1
    if n > 1:
        # Initialize an empty list to store the factors of n
        factors = []

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i is a factor of n
            if n % i == 0:
                # Add i to the list of factors of n
                factors.append(i)

        # Return False if the list of factors of n is not empty
        return len(factors) == 0

    # Return False if n is not an integer greater than 1
    return False
