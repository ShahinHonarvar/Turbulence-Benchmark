
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate from 1 to x, checking for each number if it is a left-and-right-truncatable prime number
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Initialize an empty string to store the digits of the current number
            digits = ""

            # Iterate over the digits of the current number, checking for each digit if it is zero and if removing the leading leftmost and last rightmost digits simultaneously successively would result in a one- or two-digit prime number
            for j in range(len(str(i))):
                # Check if the current digit is zero
                if str(i)[j] == "0":
                    # If the current digit is zero, break out of the inner loop and move on to the next number
                    break

                # Else, check if removing the leading leftmost and last rightmost digits simultaneously successively would result in a one- or two-digit prime number
                else:
                    # Check if removing the leading leftmost digit from the current number results in a prime number
                    if is_prime(int(str(i)[:j + 1]))) and (is_prime(int(str(i)[j + 1:])))):
                        # If removing the leading leftmost digit from the current number results in a prime number, add it to the list of prime numbers
                        primes.append(i)

                    # Check if removing the last rightmost digit from the current number results in a prime number
                    elif is_prime(int(str(i)[:j] + str(i)[j + 1:])))):
                        # If removing the last rightmost digit from the current number results in a prime number, add it to the list of prime numbers
                        primes.append(i)

    # Sort the list of prime numbers in ascending order and return it
    return sorted(primes)
