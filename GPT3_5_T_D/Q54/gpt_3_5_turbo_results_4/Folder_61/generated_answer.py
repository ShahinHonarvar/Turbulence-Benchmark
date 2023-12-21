
def all_right_truncatable_prime(numbers_tuple):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers_tuple[3]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            while num_str:
                if not is_prime(int(num_str)):
                    break
                num_str = num_str[:-1]
            else:
                right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes, reverse=True)
