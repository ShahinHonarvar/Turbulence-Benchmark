
def all_right_truncatable_prime(tuple_of_pos_int):
    x = tuple_of_pos_int[93]
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while len(str_n)>0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True

    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)
