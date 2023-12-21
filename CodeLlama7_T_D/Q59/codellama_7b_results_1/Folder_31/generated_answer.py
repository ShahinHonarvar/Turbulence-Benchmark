
def all_left_truncatable_prime(tuple):
    # Initialize list to store prime numbers
    prime_list = []

    # Loop through tuple elements
    for element in tuple:
        if is_prime(element) and is_left_truncatable_prime(element):
            prime_list.append(element)

    return sorted(prime_list, reverse=True)

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("Argument must be a positive integer.")

    # Check if n is an exact square
    root = math.sqrt(n)
    if root == int(root):
        return False

    # Check if n is prime by iterating from 2 to the square root of n
    for i in range(2, int(root) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    # Check if n contains a leading zero digit
    if str(n)[0] == "0":
        return False

    # Loop through the digits of n in reverse order
    for i in range(len(str(n)))[::-1]:
        # Remove the current digit from n and check if it is a prime number
        if not is_prime(int(str(n).replace(str(n)[i], "")))):
            return False

    return True
