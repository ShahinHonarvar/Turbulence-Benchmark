
def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[50]
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    left_right_primes = [i for i in range(x+1) if is_left_right_truncatable(i)]
    return sorted(left_right_primes, reverse=True)
