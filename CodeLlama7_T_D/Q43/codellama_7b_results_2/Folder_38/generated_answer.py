 def find_primes_between_indices(my_list):
    # Define a function to check if a number is prime or not
    def is_prime(n):
        if n == 1:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True


    # Find the prime numbers between indices 55 and 87

    prime_numbers = []

    for i in range(55, 88):

        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in ascending order

    prime_numbers.sort()

    return prime_numbers
