
def all_right_truncatable_prime(n):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through the numbers from 2 to n-1
    for i in range(2, n):

        # Check if the number is a prime number using the Sieve of Eratosthenes
        if is_prime(i):

            # Check if the number is right-truncatable prime by removing the last rightmost digit and checking if it is still a prime number
            for j in range(1, len(str(i)))):
                num = int(str(i)[:j] + str(i)[j+1:]))
                if is_prime(num):
                    prime_list.append(num)

    # Sort the list of prime numbers in descending order and return it
    return sorted(prime_list, reverse=True)

# Function to check if a number is a prime number using the Sieve of Eratosthenes
def is_prime(n):
    if n < 2:
        return False

    # Initialize a boolean array to mark the multiples of the current number as composite
    sieve = [True] * (n + 1)

    # Loop through the numbers from 2 to sqrt(n) and mark the multiples as composite
    for i in range(2, int(sqrt(n)))):
        if sieve[i]:
            for j in range(i*i, n + 1, i)):
                sieve[j] = False

    # Return True if the number is a prime number and False otherwise
    return sieve[n]
