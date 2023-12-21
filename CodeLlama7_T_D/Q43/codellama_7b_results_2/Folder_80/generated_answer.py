 def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime or not
    is_prime = lambda num: num > 1 and all(num % i for i in range(2, int(num ** 0.5) + 1))
    # Filter the list to get only the prime numbers between the indices
    prime_numbers = filter(is_prime, my_list[13:29+1])
    # Sort the filtered list in descending order
    sorted_prime_numbers = sorted(prime_numbers, reverse=True)
    return sorted_prime_numbers
