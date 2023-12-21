
def all_left_right_truncatable_prime(x):
    # Define a list to store the prime numbers
    prime_list = []
    # Iterate from 1 to x
    for i in range(1, x+1):
        # Check if the number is prime
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_list.append(i)
    # Sort the list in ascending order
    prime_list.sort()
    return prime_list

def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n+1):
        if n % i == 0:
            return False

    # If no factors have been found, n must be prime
    return True

def is_left_right_truncatable_prime(n):
    # Check if n contains any 0 digits
    for i in range(len(str(n)))):
        if str(n)[i] == '0':
            return False

    # Remove the leading and last digits of n
    leading = int(str(n)[1:-1]))
    last = int(str(n)[2:])))

    # Check if the remaining number is prime
    if is_prime(leading) and is_prime(last):
        return True

    # If the number is not prime, it is not left-and-right-truncatable prime
    return False
