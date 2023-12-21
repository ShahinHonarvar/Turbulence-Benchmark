
def all_left_right_truncatable_prime(tup):
    import sympy

    x = tup[57]
  
    def is_prime(n):
        return sympy.isprime(n)
    
    def is_truncatable(n):
        str_num = str(n)
        if '0' in str_num:
            return False
        n_len = len(str_num)
        for i in range(1, n_len):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:n_len-i])):
                return False
        return True 
    
    result = []
    for i in range(10, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    result.sort(reverse=True)
    
    return result
