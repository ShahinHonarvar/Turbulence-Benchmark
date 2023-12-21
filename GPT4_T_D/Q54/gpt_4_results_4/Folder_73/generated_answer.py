
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

    def is_all_right_truncatable(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i])) for i in range(len(str_n), 0, -1))
        
    x = numbers[97]
    right_truncatable_primes = [i for i in range(2, x) if is_all_right_truncatable(i)]
    
    return sorted(right_truncatable_primes)
