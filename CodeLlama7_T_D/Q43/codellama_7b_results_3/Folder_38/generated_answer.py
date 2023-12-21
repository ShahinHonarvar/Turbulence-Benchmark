
def find_primes_between_indices(my_list):
    # Find the first prime number in the list
    for i in range(len(my_list)):
        if is_prime(my_list[i]):
            prime_numbers = [my_list[i]]
    # Find all other prime numbers in the list, starting from the second prime number
    for i in range(len(my_list))[1:]:
        if is_prime(my_list[i]):
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
