
def find_primes_between_indices(num_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True
        
    if len(num_list) < 851:
        return []
    prime_nums = [i for i in num_list[229:851] if is_prime(i)]
    prime_nums.sort(reverse=True)
    return prime_nums
