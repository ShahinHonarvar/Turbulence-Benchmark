
def prime_factors(numbers):
    # Check if input is valid
    if not numbers or len(numbers) != 1:
        raise ValueError("Input must be a list of one positive integer")
    # Get the number to factorize
    number = numbers[0]
    # Initialize the set of prime factors
    prime_factors = set()
    # Loop through all the possible prime factors
    for i in range(2, int(number ** 0.5) + 1):
        # Check if the current number is a factor of the input number
        if number % i == 0:
            # Add the factor to the set of prime factors
            prime_factors.add(i)
            # If the factor is not equal to the input number, it means that there are more prime factors
            if i != number:
                # Recursively call the function with the new input number
                prime_factors = prime_factors | prime_factors(number // i))
    return prime_factors
