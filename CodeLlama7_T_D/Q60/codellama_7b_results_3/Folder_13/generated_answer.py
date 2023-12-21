
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, checking if each number is a left-and-right-truncatable prime number
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if isprime(i):
            # Initialize an empty string to store the current number as a string
            num_str = ""

            # Convert the current number to a string and remove any leading zeroes

            while i > 0:
                if i % 10 == 0:
                    break

                else:
                    num_str += str(i % 10)

                i //= 10


            # Check if the current number has no leading zeroes and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
            if num_str == "" or isprime(int(num_str[0])) or isprime(int(num_str[-1])):
                # If the current number is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    return sorted(prime_numbers)
