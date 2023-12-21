
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    prime_numbers = [i for i in num_list[55:77] if is_prime(i)]
    return sorted(prime_numbers)
