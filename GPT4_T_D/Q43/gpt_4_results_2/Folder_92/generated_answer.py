
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def find_primes_between_indices(lst):
    prime_nums = []
    for i in range(7, 9 + 1):
        if i < len(lst) and is_prime(lst[i]):
            prime_nums.append(lst[i])
            
    return sorted(prime_nums)
