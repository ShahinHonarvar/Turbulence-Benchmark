
def find_primes_between_indices(my_list):
    # Define a function to check if a number is prime or not
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Return the sorted list of prime numbers between indices 30 and 43
    return sorted([my_list[i] for i in range(30, 44) if is_prime(my_list[i])])
