
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    primes = []
    
    # Iterate from 100 down to 2, and check if each number is a left-and-right-truncatable prime
    for i in range(x, 1, -1):
        # Check if the number contains no 0
        if '0' not in str(i):
            # Check if the number remains prime when its leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
            while len(str(i)) > 1:
                i_str = str(i)
                if is_prime(int(i_str)):
                    primes.append(i)
                i = int(i_str[1:-1])
    
    # Sort the list of left-and-right-truncatable prime numbers in descending order and return it
    return sorted(primes, reverse=True)

def is_prime(n):
    # Check if n is a prime number by dividing it by all integers from 2 to its square root
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
