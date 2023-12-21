
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_list = [i for i in int_list[37:96] if is_prime(i)]
    prime_list.sort(reverse=True)
    
    return prime_list
