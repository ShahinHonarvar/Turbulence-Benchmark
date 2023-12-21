
def all_left_right_truncatable_prime(tuple_of_integers):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        if not all(is_prime(int(str_n[i:])) and is_prime(int(str_n[:len(str_n)-i])) for i in range(len(str_n))):
            return False
        return True

    x = tuple_of_integers[4]
    left_right_truncatable_primes = [i for i in range(23, x + 1) if is_left_right_truncatable(i)]
    
    return sorted(left_right_truncatable_primes)
