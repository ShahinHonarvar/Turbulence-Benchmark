
def prime_factors(my_list):
    # Find the index of the integer in the list that we want to factorize
    index = 43
    # Get the value of the integer at the specified index
    num = my_list[index]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all numbers from 2 to the square root of the input number
    for i in range(2, int(num ** 0.5) + 1):
        # If the current number is a factor of the input number, add it to the set of prime factors
        if num % i == 0:
            prime_factors.add(i)
    return prime_factors
