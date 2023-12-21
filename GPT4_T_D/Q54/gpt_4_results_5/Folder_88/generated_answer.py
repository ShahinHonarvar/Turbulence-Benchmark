
def all_right_truncatable_prime(tuple_of_positive_integers):
    def is_prime(n):
        if n==1:
            return False
        elif n==2:
            return True
        else:
            for x in range(2,n):
                if(n % x==0):
                    return False
            return True 

    def truncate(n):
        return int(str(n)[:-1])

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate(n)
        return True

    x = tuple_of_positive_integers[93]

    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
