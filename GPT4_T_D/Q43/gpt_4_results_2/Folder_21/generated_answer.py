
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_nums = [i for i in int_list[478:950] if is_prime(i)]
    return sorted(prime_nums, reverse=True)
