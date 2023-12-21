
def find_primes_between_indices(lst):
    primes_list = []
    def check_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for i in range(69, 85):
        if check_prime(lst[i]):
            primes_list.append(lst[i])
    
    primes_list.sort(reverse=True)
    return primes_list
