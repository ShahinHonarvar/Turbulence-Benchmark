
def find_primes_between_indices(lst):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    prime_list = [num for num in lst[23:40] if is_prime(num)]
    prime_list.sort()
    return prime_list
