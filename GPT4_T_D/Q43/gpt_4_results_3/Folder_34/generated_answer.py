
def find_primes_between_indices(int_list):
    sub_list = int_list[56:58]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [num for num in sub_list if is_prime(num)]

    return sorted(prime_numbers, reverse=True)
