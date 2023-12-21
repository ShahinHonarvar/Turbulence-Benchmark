
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_nums = []
    for num in lst[261:460]:
        if is_prime(num):
            prime_nums.append(num)
    return sorted(prime_nums)
