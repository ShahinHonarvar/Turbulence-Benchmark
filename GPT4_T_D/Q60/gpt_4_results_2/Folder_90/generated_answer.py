
def all_left_right_truncatable_prime(n_tuple):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    def check_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            str_trimmed1 = str_n[i:]
            str_trimmed2 = str_n[:len(str_n)-i]
            if not is_prime(int(str_trimmed1)) or not is_prime(int(str_trimmed2)):
                return False
        return True
        
    x = n_tuple[466]
    truncatable_primes = [i for i in range(11, x+1) if is_prime(i) and check_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
