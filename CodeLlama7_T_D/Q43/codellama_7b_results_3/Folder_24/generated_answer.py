
def find_primes_between_indices(my_list):
    # Initialize variables for the function
    prime_numbers = []
    index_start = 38
    index_end = 55
    # Iterate through the list and check if each element is a prime number
    for i in range(index_start, index_end + 1):
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
