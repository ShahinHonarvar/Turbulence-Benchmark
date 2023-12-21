
def all_right_truncatable_prime(nums):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through each number in the tuple
    for num in nums:
        # Check if the number is a prime number
        if is_prime(num):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(num)

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
