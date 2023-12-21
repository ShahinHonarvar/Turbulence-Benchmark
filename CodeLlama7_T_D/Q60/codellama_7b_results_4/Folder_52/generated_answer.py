
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    # Filter the list to only include left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = []
    for prime in prime_numbers:
        if is_left_right_truncatable_prime(prime):
            left_right_truncatable_prime_numbers.append(prime)
    # Sort the list in descending order
    sorted_list = sorted(left_right_truncatable_prime_numbers, reverse=True)
    return sorted_list

# Check if a number is prime by iterating from 2 to the square root of the number
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

# Check if a number is a left-and-right-truncatable prime number by iterating from 1 to the length of the number and checking if the number remains prime after removing the leading leftmost and last rightmost digits.
def is_left_right_truncatable_prime(n):
    for i in range(1, len(str(n)))):
        if not is_prime(int(str(n)[i:]))) or not is_prime(int(str(n)[:-i]))) :
            return False

    return True
