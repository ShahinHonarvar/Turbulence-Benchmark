
def find_primes_between_indices(my_list):
    # Define a function to check if a number is prime or not
    def is_prime(n):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    # Define a list to store the prime numbers

    prime_numbers = []

    # Iterate through the list of integers and check for each number if it is prime or not

    for i in range(608, 879):
        if is_prime(i):
            prime_numbers.append(i)

    # Return the sorted list of all prime numbers from index 608 to index 878, both inclusive

    return sorted(prime_numbers, reverse=True)
