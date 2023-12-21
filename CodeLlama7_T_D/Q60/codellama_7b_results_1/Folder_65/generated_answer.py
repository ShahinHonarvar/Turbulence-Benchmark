
def all_left_right_truncatable_prime(x):
    # Define a set to store prime numbers
    prime_numbers = set()

    # Check if x is a prime number and add it to the set
    if is_prime(x) == True:
        prime_numbers.add(x)

    # Check for left-and-right-truncatable prime numbers less than or equal to x
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime(i) == True:
            # Define a list to store the digits of i
            digit_list = []

            # Store the digits of i in the list
            while i > 0:
                digit_list.append(i % 10)

                # Remove the last digit from i
                i //= 10

            # Check if the leading leftmost and last rightmost digits of i are simultaneously successively removed down to a one- or two-digit prime
            if is_prime(int(''.join(map(str, digit_list[:-2]))))) == True:
                prime_numbers.add(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(list(prime_numbers)), key=lambda x: x[1])
