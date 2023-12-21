
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([x for i,x in enumerate(int_list[61:81]) if is_prime(x)], reverse=True)
