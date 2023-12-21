
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime or not
    is_prime = lambda num: num > 1 and all(num % i for i in range(2, int(num ** 0.5) + 1))
    # Get the indices of the list that correspond to the desired range
    start_index = 24
    end_index = 32
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list and check if each number is prime or not
    for i in range(start_index, end_index + 1):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
