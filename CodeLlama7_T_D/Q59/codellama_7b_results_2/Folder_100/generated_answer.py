
def all_left_truncatable_prime(x):
    # Define a function to check if a number is prime or not
    def is_prime(n):
        if n == 1 or n == 0:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    # Define a function to generate all left-truncatable prime numbers less than x

    def generate_left_truncatable_prime(x):
        prime_numbers = []

        for i in range(2, x + 1):
            if is_prime(i) and str(i)[::-1] == str(i)[1:]:
                prime_numbers.append(i)

        return sorted(prime_numbers)

    # Return the list of all left-truncatable prime numbers less than x

    return generate_left_truncatable_prime(x)
