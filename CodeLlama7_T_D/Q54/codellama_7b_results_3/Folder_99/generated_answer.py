
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple elements and check if each element is a prime number
    for i in range(len(tuple)):
        # Check if the current element is a prime number using the is_prime function
        if is_prime(tuple[i]):
            # If the current element is a prime number, add it to the prime_numbers list
            prime_numbers.append(tuple[i])

    # Iterate over the prime numbers and check if each number is right-truncatable prime
    for i in range(len(prime_numbers)):
        # Check if the current prime number is a right-truncatable prime using the is_right_truncatable_prime function
        if is_right_truncatable_prime(prime_numbers[i]):
            # If the current prime number is a right-truncatable prime, add it to the sorted list of all right-truncatable prime numbers less than x
            sorted_list.append(prime_numbers[i])

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(sorted_list)

# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is a power of 2
        if n & (n - 1) == 0:
            # If n is a power of 2, it cannot be prime so return False
            return False

        # Iterate from 2 to sqrt(n) and check if n is divisible by any number between 2 and sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):
            # If n is divisible by any number between 2 and sqrt(n), it is not prime so return False
            if n % i == 0:
                return False

    # If n is less than or equal to 1, it is not prime so return False
    else:
        return False

# Function to check if a number is a right-truncatable prime or not
def is_right_truncatable_prime(n):
    # Check if n is a prime number using the is_prime function
    if is_prime(n):
        # Iterate over the digits of the current number
        for i in range(len(str(n)))):
            # Check if the current digit is the last rightmost digit of the current number
            if str(n)[i] == str(n)[-1]:
                # If the current digit is the last rightmost digit of the current number, check if the current number is still a prime number after removing the last rightmost digit
                if is_prime(int(str(n)[:-1])):
                    # If the current number is still a prime number after removing the last rightmost digit, return True
                    return True

            # Check if the current digit is not the last rightmost digit of the current number
            else:
                # If the current digit is not the last rightmost digit of the current number, check if the current number is still a prime number after removing the last rightmost digit
                if not is_prime(int(str(n)[:-1]))):
                    # If the current number is not a prime number after removing the last rightmost digit, return False
                    return False
