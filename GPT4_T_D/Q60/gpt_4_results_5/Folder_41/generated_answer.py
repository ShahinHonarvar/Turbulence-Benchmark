
def all_left_right_truncatable_prime(list1):
    x = list1[46]
    primes = []
    def is_prime(n):
        if n==1:
            return False
        elif n==2:
            return True
        else:
            for x in range(2,n):
                if n % x == 0:
                    return False
            return True  
    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True
    for i in range (2, x+1):
        if is_prime(i):
            if is_truncatable_prime(i):
                primes.append(i)
    primes.sort(reverse=True)
    return primes
