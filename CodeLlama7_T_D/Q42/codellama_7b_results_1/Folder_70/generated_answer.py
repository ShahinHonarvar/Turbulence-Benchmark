
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the list of integers
    for i in my_list:
        # Check if the integer is a prime number
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_factors.add(i)
    return prime_factors
