
def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers between indices
    prime_numbers = []

    # Iterate through the list from index 131 to index 815
    for i in range(131, 816):
        # Check if the current number is divisible by any other number in the range
        is_divisible = False
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_divisible = True
                break

        # If the current number is prime, add it to the list
        if not is_divisible:
            prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers
