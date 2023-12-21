
def all_right_truncatable_prime(tuple_of_numbers):
    def is_prime(n):
        if n==1:
            return False
        elif n==2:
            return True
        else:
            for x in range(2,n):
                if(n%x==0):
                    return False
            return True 

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        elif n < 10:
            return True
        else:
            return is_right_truncatable_prime(n // 10)

    x = tuple_of_numbers[93]
    right_truncatable_primes = [i for i in range(1, x) if is_right_truncatable_prime(i)]
    right_truncatable_primes.sort()
    return  right_truncatable_primes
