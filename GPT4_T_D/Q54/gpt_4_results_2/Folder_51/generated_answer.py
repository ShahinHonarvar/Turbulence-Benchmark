
def all_right_truncatable_prime(tup):
    x = tup[54]
    right_truncate_primes = []
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    for num in range(2, x):
        str_num = str(num)
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[:-1]
        else:
            right_truncate_primes.append(num)
    return sorted(right_truncate_primes)
