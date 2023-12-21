
def find_primes_between_indices(list_of_integers):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n%2 == 0 or n%3 == 0:
            return False
        i = 5
        while(i * i <= n):
            if (n%i == 0 or n%(i + 2) == 0):
                return False
            i += 6
        return True
    
    subset = list_of_integers[20:26]
    primes = [i for i in subset if is_prime(i)]
    primes.sort(reverse=True)
    return primes
