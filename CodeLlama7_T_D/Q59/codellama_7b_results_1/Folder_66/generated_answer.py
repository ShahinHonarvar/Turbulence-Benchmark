
def all_left_truncatable_prime(tuple):
# Get the integer at index 25
x = tuple[25]
# Create an empty list to store the results
results = []

# Iterate through the numbers less than x
for num in range(2, x):

    # Check if the number is a prime number
    if is_prime(num):

        # Check if the number is left-truncatable prime
        if is_left_truncatable_prime(num):

            # Add the number to the results list
            results.append(num)

# Sort the results list in descending order
results.sort(reverse=True)

# Return the sorted results list
return results


def is_prime(num):

    # Check if the number is divisible by 1 or itself
    for i in range(2, num + 1):
        if num % i == 0:
            return False

    # If the number is not divisible by any other number, it is prime
    return True


def is_left_truncatable_prime(num):

    # Check if the number contains a 0
    if '0' in str(num):
        return False

    # Remove the leading leftmost digit of the number
    num = int(str(num)[1:])

    # Check if the resulting number is prime
    return is_prime(num)
