
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    primes = []
    
    # Iterate from 10 to x, where x is the integer at index 835
    for i in range(10, x+1):
        # Check if the current number is a left-and-right-truncatable prime number
        if is_left_right_truncatable_prime(i):
            primes.append(i)
    
    return sorted(primes)

def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0
    if '0' in str(n):
        return False
    
    # Check if the number is a prime number
    if not is_prime(n):
        return False
    
    # Check if the leftmost and rightmost digits are simultaneously removed down to a one- or two-digit prime number
    for i in range(1, len(str(n))//2+1):
        left = int(str(n)[:i])
        right = int(str(n)[-i:])
        if not is_prime(left) or not is_prime(right):
            return False
    
    return True

def is_prime(n):
    # Check if the number is a prime number
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
