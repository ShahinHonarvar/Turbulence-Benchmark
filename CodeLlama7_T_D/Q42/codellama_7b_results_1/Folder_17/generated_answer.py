
def prime_factors(numbers):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the numbers in the list
    for number in numbers:
        # Check if the number is prime by dividing it by all other numbers less than or equal to its square root
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        # If the number is prime, add it to the set of prime factors
        if is_prime:
            prime_factors.add(number)

    return prime_factors
