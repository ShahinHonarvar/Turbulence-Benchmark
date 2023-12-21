
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x
    for number in range(1, x + 1):
        # Check if the number is a prime number
        if number == 1 or number % 2 == 0:
            continue

        # Initialize a boolean variable to indicate whether the number is left-and-right-truncatable prime
        is_prime = True

        # Loop through all digits of the number from right to left
        for digit in str(number)[::-1]:
            # Check if the current digit is 0
            if digit == '0':
                # If the current digit is 0, set the boolean variable to False and break out of the loop
                is_prime = False
                break

        # If the number is a left-and-right-truncatable prime number, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(number)

    # Sort the list of prime numbers in descending order and return it
    return sorted(prime_numbers, reverse=True)
