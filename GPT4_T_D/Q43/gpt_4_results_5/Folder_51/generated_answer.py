
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_nums = [x for x in int_list[14:69] if is_prime(x)]
    prime_nums.sort(reverse=True)
    
    return prime_nums
