
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    primes = []
    for num in lst[31:93]:
        if is_prime(num):
            primes.append(num)

    primes.sort(reverse = True)
    return primes
