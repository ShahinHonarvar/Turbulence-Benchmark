
def find_primes_between_indices(lst):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    primes = [i for i in lst[27:87] if is_prime(i)]
    primes.sort(reverse=True)
    return primes
