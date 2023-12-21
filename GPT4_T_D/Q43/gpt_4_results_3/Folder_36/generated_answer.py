
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    for num in num_list[229:851]:
        if is_prime(num):
            prime_numbers.append(num)
    
    return sorted(prime_numbers, reverse=True)
