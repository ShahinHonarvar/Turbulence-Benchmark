
def find_primes_between_indices(my_list):
    # Initialize variables
    prime_numbers = []
    start_index = 157
    end_index = 735
    # Iterate through the list and check if each element is prime
    for i in range(start_index, end_index + 1):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    # Sort the prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
