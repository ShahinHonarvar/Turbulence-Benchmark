
def find_primes_between_indices(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    for i in range(20, 26):
        if is_prime(numbers[i]):
            prime_list.append(numbers[i])
    
    return sorted(prime_list, reverse=True)
