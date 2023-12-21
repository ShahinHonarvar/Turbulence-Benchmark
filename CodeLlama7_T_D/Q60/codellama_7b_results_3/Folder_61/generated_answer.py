
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the numbers from 1 to x
    for num in range(1, x + 1):

        # Check if the number is a prime number
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                # If the number is a prime number and it is left-and-right-truncatable prime number
                if is_left_right_truncatable_prime(num):
                    prime_numbers.append(num)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

def is_left_right_truncatable_prime(num):
    # Check if the number contains 0
    if '0' in str(num):
        return False

    # Check if the number is a prime number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    # Check if the number is left-and-right-truncatable prime number
    for i in range(3):
        temp = num

        # Remove the leading leftmost and last rightmost digits from the number
        while temp % 10 == 0:
            temp //= 10

        # Check if the number is a prime number
        if not is_prime(temp):
            return False

    # If the number is a left-and-right-truncatable prime number, return True
    return True

def is_prime(num):
    # Check if the number is greater than 1
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

    # If the number is a prime number, return True
    return True
