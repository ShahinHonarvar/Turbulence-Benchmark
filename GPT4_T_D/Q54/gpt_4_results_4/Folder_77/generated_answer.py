
def all_right_truncatable_prime(tpl):
    x = tpl[767]
    all_primes = []

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range (2, n):
                if n % i == 0:
                    return False
            return True

    def truncatable(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if is_prime(int(str_num[i:])) == False:
                return False
        return True

    for i in range(2, x):
        if truncatable(i):
            all_primes.append(i)

    return sorted(all_primes, reverse = True)
