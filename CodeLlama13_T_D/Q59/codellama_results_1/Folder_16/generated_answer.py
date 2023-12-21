
def all_left_truncatable_prime(x):
    # Create a list of all left-truncatable prime numbers less than x
    prime_list = []
    for i in range(2, x+1):
        if is_left_truncatable_prime(i):
            prime_list.append(i)
    # Sort the list in ascending order
    return sorted(prime_list)

def is_left_truncatable_prime(n):
    # Check if n is a left-truncatable prime number
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
