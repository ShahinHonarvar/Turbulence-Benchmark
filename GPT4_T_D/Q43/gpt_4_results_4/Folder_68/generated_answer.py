
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        return False

    primes = [num for num in num_list[1:6] if is_prime(num)]
    primes.sort()

    return primes
