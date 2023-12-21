
def find_primes_between_indices(my_list):
    # Find the index of the first prime number in the list
    start_index = next((i for i, x in enumerate(my_list) if is_prime(x)))))

    # Find the index of the last prime number in the list
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if is_prime(x))), start_index))

    # Return the sorted list of prime numbers between the indices
    return sorted(my_list[start_index:end_index+1], key=lambda x: -x)

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
