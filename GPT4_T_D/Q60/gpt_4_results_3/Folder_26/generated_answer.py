
def all_left_right_truncatable_prime(tuple_of_integers):
    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1 or n == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n): return False
        n_str = str(n)
        for i in range(len(n_str)):
            if not (is_prime(int(n_str[i:])) and is_prime(int(n_str[:len(n_str)-i]))):
                return False
        return True
        
    x = tuple_of_integers[81]
    primes = [i for i in range(x + 1) if is_left_right_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes
