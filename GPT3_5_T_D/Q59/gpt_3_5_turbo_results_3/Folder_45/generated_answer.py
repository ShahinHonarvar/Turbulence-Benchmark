
def all_left_truncatable_prime(tuple_of_positive_integers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    result = []
    x = tuple_of_positive_integers[61]
    
    def is_left_truncatable_prime(num):
        num_str = str(num)
        
        if '0' in num_str:
            return False
        
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
            
        return True
    
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
            
    return sorted(result)
