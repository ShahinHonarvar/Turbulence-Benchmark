
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_nums = [i for i in lst[19:72] if is_prime(i)]
    prime_nums.sort()
    return prime_nums
