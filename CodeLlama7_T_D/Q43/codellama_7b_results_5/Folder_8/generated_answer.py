
def find_primes_between_indices(my_list):
    # Find the first prime number in the range
    start_index = 36
    for i in range(start_index, len(my_list)):
        if is_prime(my_list[i]):
            # If a prime number is found, return the sorted list of all prime numbers from index 36 to index 71, both inclusive
            prime_numbers = []
            for j in range(start_index, i + 1):
                if is_prime(my_list[j]):
                    prime_numbers.append(my_list[j])
            return sorted(prime_numbers, reverse=True)
    # If no prime number exists in the specified range, return an empty list
    return []

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
