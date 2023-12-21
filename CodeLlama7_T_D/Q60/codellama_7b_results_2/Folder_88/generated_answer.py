
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if the number is a prime number using the Sieve of Eratosthenes
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                # If the number is a prime number, check if it is left-and-right-truncatable prime number
                flag = True

                for k in range(len(str(i)) - 1):
                    if str(i)[k] != '0':
                        break

                for l in range(len(str(i)) - 2, -1, -1):
                    if str(i)[l] != '0':
                        break

                if flag and k >= l:
                    # If the number is a left-and-right-truncatable prime number, add it to the list of prime numbers
                    prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in ascending order
    return sorted(prime_numbers)
