
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    def check_truncatable(num):
        for i in range(len(str(num))):
            new_num = int(str(num)[:i+1])
            if not is_prime(new_num):
                return False
        return True

    x = tup[177]
    truncatable_primes = []
    for i in range(2,x):
        if check_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
