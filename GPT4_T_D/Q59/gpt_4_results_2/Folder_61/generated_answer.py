
def all_left_truncatable_prime(tuple):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return num != 1

    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return True

    x = tuple[3]
    primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num):
            primes.append(num)
            
    return sorted(primes, reverse=True)
