
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes_list = [i for i in int_list[28:45] if is_prime(i)]
    primes_list.sort()
    return primes_list
