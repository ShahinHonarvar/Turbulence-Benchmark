
# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to get left-and-right-truncatable prime numbers
def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[65]
    
    # Loop through numbers less than or equal to x
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue

        # Check if the number remains prime after truncating
        temp = str(num)
        while len(temp) > 2:
            temp = temp[1:-1]
            if not is_prime(int(temp)):
                break
        else:
            primes.append(num)

    primes.sort(reverse=True)
    return primes
