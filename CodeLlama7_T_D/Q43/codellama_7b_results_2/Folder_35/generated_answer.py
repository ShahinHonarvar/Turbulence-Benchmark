
def find_primes_between_indices(my_list):
    # Define a list to store the prime numbers between indices
    prime_numbers = []

    # Iterate through the list of integers, starting from index 112
    for i in range(112, len(my_list)):
        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(i ** 0.5) + 1):
            # If the current element is divisible by any number between 2 and the square root of the current element, it is not prime
            if i % j == 0:
                break

        else:

            # If the current element is not divisible by any number between 2 and the square root of the current element, it is prime
            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)
