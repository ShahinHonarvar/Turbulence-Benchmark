
def all_left_right_truncatable_prime(nums):
    # Create a list to store the prime numbers
    prime_list = []

    for num in nums:

        # Check if the number is a prime number

        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime number

            if is_left_right_truncatable_prime(num):

                # Add the prime number to the list

                prime_list.append(num)

    return prime_list

def is_prime(n):

    # Check if n is a positive integer

    if not isinstance(n, int) or n < 2:

        return False


    # Check if n is divisible by any number between 2 and the square root of n

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True

def is_left_right_truncatable_prime(n):

    # Check if n is a prime number

    if not is_prime(n):

        return False


    # Check if the leading leftmost and last rightmost digits of n are both 1

    if str(n)[0] != "1" or str(n)[-1] != "1":

        return False


    # Check if removing the leading leftmost digit from n results in a prime number

    if not is_prime(int(str(n)[:-1]))):

        return False


    # Check if removing the last rightmost digit from n results in a prime number

    if not is_prime(int(str(n)[1:]))):

        return False


    return True
