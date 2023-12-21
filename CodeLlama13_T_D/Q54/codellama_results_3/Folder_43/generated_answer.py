
def all_right_truncatable_prime(numbers):
    # Initialize an empty list to store the right-truncatable prime numbers
    right_truncatable_primes = []
    
    # Iterate over the tuple of positive integers
    for number in numbers:
        # Check if the current number is a right-truncatable prime
        if is_right_truncatable_prime(number):
            # If it is, add it to the list of right-truncatable primes
            right_truncatable_primes.append(number)
    
    # Return the sorted list of right-truncatable prime numbers
    return sorted(right_truncatable_primes, reverse=True)
```
```
def is_right_truncatable_prime(number):
    # Check if the number is a prime number
    if not is_prime(number):
        return False
    
    # Iterate over the digits of the number, starting from the rightmost digit
    for i in range(len(str(number))-1, -1, -1):
        # Check if the current digit is not equal to 0
        if str(number)[i] != '0':
            # If it is not, remove the last rightmost digit and check if the result is still a prime number
            if not is_prime(int(str(number)[:i+1])):
                return False
    
    # If all digits are 0, return True
    return True
```
```
def is_prime(number):
    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    # If the number is not divisible by any number between 2 and the square root of the number, it is prime
    return True
