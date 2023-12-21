
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_list.append(i)
    return prime_list

def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

# Check if n is divisible by 2 to n-1
for i in range(2, n+1):
    if n % i == 0:
        return False

return True

def is_left_right_truncatable_prime(n):
    # Initialize a string representation of the number
    num_str = str(n)

# Check if the number contains any 0 digits
if '0' in num_str:
    return False

# Remove the leading leftmost and last rightmost digits from the string representation of the number
num_str = num_str[1:-1]

# Convert the modified string representation of the number to an integer
n = int(num_str)

# Check if the modified integer is a prime number
if is_prime(n):
    return True
