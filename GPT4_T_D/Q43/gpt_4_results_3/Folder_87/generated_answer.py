
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n%i == 0:
                return False
        return True
    
    prime_numbers = [num for num in int_list[11:42] if is_prime(num)]
    prime_numbers.sort(reverse=True)
    
    return prime_numbers
