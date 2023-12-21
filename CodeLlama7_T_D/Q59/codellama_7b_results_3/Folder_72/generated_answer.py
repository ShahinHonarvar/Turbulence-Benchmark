
def all_left_truncatable_prime(nums):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate over the input tuple
    for num in nums:
        if is_prime(num) and is_left_truncatable_prime(num):
            prime_numbers.append(num)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    # Check if the number contains a zero digit
    if '0' in str(n):
        return False

    # Iterate over all the leading leftmost digits of the number
    for i in range(1, len(str(n)))):
        # Calculate the resulting number after removing the current digit
        result = int(str(n)[:i] + str(n)[i+1:]))
        # Check if the resulting number is prime
        if not is_prime(result):
            return False

    return True
