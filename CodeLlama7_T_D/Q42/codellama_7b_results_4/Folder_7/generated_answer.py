
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the elements of the list
    for element in my_list:
        # Check if the element is a prime number
        if is_prime(element):
            # If it is, add it to the set of prime factors
            prime_factors.add(element)
    return prime_factors

def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

# Check if n is divisible by 2 to 10
for i in range(2, 11):
    if n % i == 0:
        return False
