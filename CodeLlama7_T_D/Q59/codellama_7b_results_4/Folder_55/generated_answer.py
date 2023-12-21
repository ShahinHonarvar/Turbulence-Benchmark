
def all_left_truncatable_prime(tuple):
    # Initialize an empty list for the results
    results = []

    # Loop through each number in the tuple
    for number in tuple:
        # Check if the current number is a prime number
        if is_prime(number):
            # If it is, loop through all possible left-truncatable prime numbers less than the current number
            for i in range(10):
                # Calculate the current left-truncatable prime number
                current = int(str(number)[1:] + str(i)))

                # Check if the current number is a prime number and add it to the results list if it is
                if is_prime(current):
                    results.append(current)

            # Sort the results list in descending order
            results = sorted(results, reverse=True)

        # Return the results list
        return results

def is_prime(number):
    # Check if the number is less than 2 or not divisible by 2
    if number < 2 or number % 2 == 0:
        # If it is, return False
        return False

    # Otherwise, loop through all numbers up to and including the square root of the current number
    for i in range(2, int(math.sqrt(number)) + 1):
        # Check if the current number is divisible by any number other than 1 or itself
        if number % i == 0:
            # If it is, return False
            return False

    # If none of the above conditions are met, return True
    return True
