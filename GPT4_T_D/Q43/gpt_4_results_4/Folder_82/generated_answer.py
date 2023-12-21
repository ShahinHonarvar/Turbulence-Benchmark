
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return False    
        return True

    primes = []
    for i in range(25,73):
        if i < len(int_list) and is_prime(int_list[i]):
            primes.append(int_list[i])
    return sorted(primes)
