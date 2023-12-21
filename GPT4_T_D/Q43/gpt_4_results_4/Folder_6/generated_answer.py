
def find_primes_between_indices(lst):
    def check_prime(n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    primes = [i for i in lst[89:(93+1)] if check_prime(i)]
    return sorted(primes, reverse=True)
