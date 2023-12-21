
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple and check for each element if it is a prime number and if it is right-truncatable prime number
    for x in tuple:
        # Check if x is a prime number using the built-in function is_prime
        if is_prime(x):
            # Check if x is a right-truncatable prime number by iterating over the digits of x from right to left and checking if each digit is divisible by 2, 3, 5, and 7. If any digit is not divisible by at least one of these numbers, then x is not a right-truncatable prime number
            is_right_truncatable = True
            for i in range(len(str(x)) - 1, -1, -1)):
                if str(x)[i] % 2 == 0 or str(x)[i] % 3 == 0 or str(x)[i] % 5 == 0 or str(x)[i] % 7 == 0:
                    is_right_truncatable = False
            # If x is both a prime number and a right-truncatable prime number, then add it to the list of prime numbers
            if is_prime and is_right_truncatable:
                prime_numbers.append(x)
    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers)
