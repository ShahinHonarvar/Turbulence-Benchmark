
def all_right_truncatable_prime(numbers):
    from sympy import isprime

    def is_right_truncatable_prime(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True

    x = numbers[30]
 
    result = [i for i in range(2, x) if is_right_truncatable_prime(i)]
  
    result.sort(reverse=True)

    return result
