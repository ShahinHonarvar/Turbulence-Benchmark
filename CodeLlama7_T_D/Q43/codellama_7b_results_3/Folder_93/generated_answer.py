 def find_primes_between_indices(my_list):
    # Find the index of the first prime number in the list
    first_prime = next((i for i, x in enumerate(my_list) if is_prime(x)), None)
    # If there are no prime numbers in the list, return an empty list
    if first_prime is None:
        return []

    # Find the index of the last prime number in the list

    last_prime = next((i for i, x in enumerate(my_list) if is_prime(x))), None)
    # If there are no prime numbers in the list, return an empty list
    if last_prime is None:
        return []

    # Return the sorted list of all prime numbers from index 70 to index 71, both inclusive

    return sorted(my_list[first_prime:last_prime+1], reverse=True)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
