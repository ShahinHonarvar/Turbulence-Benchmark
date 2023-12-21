
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through each element in the tuple
    for i in range(len(tuple)):
        current_num = tuple[i]

        # Check if the current number is prime
        if is_prime(current_num):
            # Add the current number to the list of prime numbers
            prime_list.append(current_num)

        # If the current number has more than one digit, continue checking
        while len(str(current_num)) > 1:
            # Remove the leftmost digit from the current number
            current_num = int(str(current_num)[1:]))

            # Check if the resulting number is prime
            if is_prime(current_num):
                # Add the resulting number to the list of prime numbers
                prime_list.append(current_num)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_list, reverse=True)

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
