
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i) and left_and_right_truncatable_prime(i):
            prime_list.append(i)
    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in descending order
    return sorted(prime_list, reverse=True)
def is_prime(n):
    # Check if n is a prime number

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def left_and_right_truncatable_prime(n):
# Check if n is a left-and-right-truncatable prime number

for i in range(len(str(n)))):
    # Check if the leading digit of n is 0. If it is, return False.
    if str(n)[i] == "0":
        return False

    # Check if the last rightmost digit of n is a prime number. If it is not, return False.
    if not is_prime(int(str(n)[:-1]))):
        return False
