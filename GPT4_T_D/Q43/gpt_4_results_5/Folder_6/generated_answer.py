
def find_primes_between_indices(integer_list):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    from_index = max(89, 0)
    to_index = min(93, len(integer_list) - 1)
    primes = [i for i in integer_list[from_index:to_index+1] if is_prime(i)]
    primes.sort(reverse=True)
    return primes
