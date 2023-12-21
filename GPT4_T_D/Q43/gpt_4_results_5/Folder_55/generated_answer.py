
def find_primes_between_indices(lst):
    primes = []
    
    def check_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    for i in range(2, 3):
        if check_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)
