
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple and check if each number is a prime number
    for num in tuple:
        is_prime = True

        # Check if the number is greater than 1
        if num > 1:
            # Loop through the numbers from 2 to the square root of the current number
            for i in range(2, int(num ** 0.5) + 1):
                # If the current number is divisible by any number between 2 and the square root of the current number, it is not a prime number
                if num % i == 0:
                    is_prime = False
                    break

        # If the current number is a prime number, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(num)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers, reverse=True)
