
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    prime_list = []
    for index in range(25, 73):
        if is_prime(numbers[index]):
            prime_list.append(numbers[index])
    return sorted(prime_list)
