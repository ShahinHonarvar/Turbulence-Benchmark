
def all_right_truncatable_prime(num_tuple):
    x = num_tuple[54]
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
    def is_right_truncatable(n):
        str_num = str(n)
        for _ in range(len(str_num)):
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True
    primes = [i for i in range(2,x) if is_prime(i) and is_right_truncatable(i)]
    primes.sort(reverse=True)
    return primes
