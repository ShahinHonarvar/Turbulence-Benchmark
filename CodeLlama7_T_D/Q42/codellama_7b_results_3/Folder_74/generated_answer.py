
def prime_factors(my_list):
    # Get the integer at index 48
    num = my_list[48]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        # Check if i is a factor of num
        if num % i == 0:
            # If it is a prime factor, add it to the set
            if is_prime(i):
                prime_factors.add(i)
            # Otherwise, it is a composite factor, so break out of the loop
            else:
                break

    # Return the set of all prime factors of num
    return prime_factors

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If any multiple is found, return False
            if n % i == 0:
                return False

    # If no multiples are found, return True
    return True
