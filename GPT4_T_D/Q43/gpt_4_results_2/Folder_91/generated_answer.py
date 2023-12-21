
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    primes_list = []
    
    for i in range(num_list[0], num_list[1] + 1):
        if is_prime(i):
            primes_list.append(i)
    
    primes_list.sort()
    
    return primes_list
