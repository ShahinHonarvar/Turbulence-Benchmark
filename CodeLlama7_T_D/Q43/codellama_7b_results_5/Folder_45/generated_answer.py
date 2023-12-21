 def find_primes_between_indices(my_list):
    # Initialize variables
    prime_numbers = []
    start_index = 48
    end_index = 92
    # Iterate through the list and check for prime numbers
    for i in range(start_index, end_index + 1):
        # Check if the number is divisible by any other number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers
