
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True
    
    primes = [num for num in int_list[60:96] if is_prime(num)]
    return sorted(primes)
