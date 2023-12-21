
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n == 2 or n == 3: 
            return True
        if n < 2 or n%2 == 0: 
            return False
        if n < 9:
            return True
        if n%3 == 0: 
            return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: 
                return False
            if n%(f+2) == 0: 
                return False
            f +=6
        return True    

    def is_right_truncatable(n):
        n_str = str(n)
        # remove the last digit until there is no digit left
        while len(n_str) > 0:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True

    x = t[79]
    primes = [i for i in range(x) if is_prime(i) and is_right_truncatable(i)]
    primes.sort(reverse = True)
    return primes
