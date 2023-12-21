
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 38 to 55
    for i in range(38, 56):
        # Check if the current element is divisible by any of the previous prime numbers
        is_prime = True
        for j in range(i - 1, -1, -1):
            if my_list[i] % my_list[j] == 0:
                is_prime = False
                break

        # If the current element is prime, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers
