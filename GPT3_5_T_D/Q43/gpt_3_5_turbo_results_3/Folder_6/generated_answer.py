
def find_primes_between_indices(lst):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    for num in lst[89:94][::-1]:
        if is_prime(num):
            prime_list.append(num)
            
    return prime_list
