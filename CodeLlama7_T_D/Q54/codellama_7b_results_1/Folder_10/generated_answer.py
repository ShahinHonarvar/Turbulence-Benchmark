
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    results = []

    # Loop through each number in the tuple
    for num in tuple:
        # Check if the number is a prime number
        if is_prime(num):
            # If it is, check if it is right-truncatable
            if is_right_truncatable(num):
                # If it is, add it to the results list
                results.append(num)

    # Sort the results list in descending order
    results.sort(reverse=True)

    # Return the sorted list of right-truncatable prime numbers less than x
    return results

# Define a function to check if a number is prime
def is_prime(num):
    # Check if the number is divisible by 2
    if num % 2 == 0:
        # If it is, return False
        return False

    # Check if the number is divisible by any other odd numbers up to its square root
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            # If it is, return False
            return False

    # If none of the above conditions are met, return True
    return True

# Define a function to check if a number is right-truncatable
def is_right_truncatable(num):
    # Check if the number is divisible by 10
    if num % 10 == 0:
        # If it is, return False
        return False

    # Check if the number has the same remainder when divided by 10 as it does when divided by its rightmost digit
    if (num % 10) != ((num // 10) % 10):
        # If it does not, return False
        return False

    # If none of the above conditions are met, return True
    return True
