
def find_primes_between_indices(numbers_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    results = []
    list_length = len(numbers_list)
    if list_length > 89:
        for i in range(87,90):
            if is_prime(numbers_list[i]):
                results.append(numbers_list[i])
    return sorted(results)
