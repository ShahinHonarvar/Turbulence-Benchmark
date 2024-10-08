
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_list.append(i)
    # Sort the list of prime numbers in descending order
    prime_list = sorted(prime_list, reverse=True)
    return prime_list

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_left_right_truncatable_prime(n):
    # Check if the number contains any zeros
    if '0' in str(n):
        return False

    # Check if the number is prime when all leading digits are removed
    for i in range(1, len(str(n)))):
        if not is_prime(int(str(n)[:i]))) or not is_prime(int(str(n)[-i:]))) or n != int(str(n))):
            return False

    return True
