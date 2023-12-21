
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n%2 == 0 or n%3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    prime_list = []
    for index in range(424, 553):
        if index < len(int_list) and is_prime(int_list[index]):
            prime_list.append(int_list[index])
            
    return sorted(prime_list, reverse=True)
