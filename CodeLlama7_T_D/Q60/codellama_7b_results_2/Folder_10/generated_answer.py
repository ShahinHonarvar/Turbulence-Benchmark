
def all_left_right_truncatable_prime(x):
    # Define a lambda function to check if a number is prime or not
    is_prime = lambda n: (n > 1 and n % 2 != 0)
    # Create an empty list to store the left-and-right-truncatable prime numbers
    prime_numbers = []
    # Iterate from 1 to x and check if each number is a prime and left-and-right-truncatable prime number or not
    for i in range(1, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_numbers.append(i)
    # Sort the list of left-and-right-truncatable prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers
