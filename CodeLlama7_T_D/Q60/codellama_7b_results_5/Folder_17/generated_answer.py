
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x (inclusive) and check if each number is a left-and-right-truncatable prime number
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number can be divided by any other prime numbers without leaving any digits
            is_left_right_truncatable = True
            for j in range(2, int(math.sqrt(i)) + 1)):
                if i % j == 0:
                    is_left_right_truncatable = False
                    break

            # If the current number is a left-and-right-truncatable prime number, add it to the list of prime numbers
            if is_left_right_truncatable:
                prime_list.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x in descending order
    return sorted(prime_list, reverse=True)
