
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []

    # Iterate from 2 to x
    for i in range(2, x + 1):
        # If i is a prime number and it is left-and-right-truncatable prime number
        if is_prime(i) and is_left_right_truncatable_prime(i):
            results.append(i)
    # Sort the results in descending order
    results = sorted(results, reverse=True)
    return results

# Check if a number is prime or not
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the loop completes normally, return True
    return True

# Check if a number is left-and-right-truncatable prime or not
def is_left_right_truncatable_prime(n):
    # Check if n contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the leading digit of n is equal to the last rightmost digit of n
    if int(str(n)[0]) != int(str(n)[-1]):
        return False

    # Check if the trailing digit of n is equal to the first leftmost digit of n
    if int(str(n)[-1]) != int(str(n)[0])):
        return False

    # If the loop completes normally, return True
    return True
