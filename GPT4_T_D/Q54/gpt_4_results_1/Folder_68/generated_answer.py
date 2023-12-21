
def all_right_truncatable_prime(tuple_of_int):

    def right_truncatable(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = tuple_of_int[1]
    right_truncatable_primes = []
    
    for num in range(2, x):
        if right_truncatable(num):
            right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes, reverse=True)
