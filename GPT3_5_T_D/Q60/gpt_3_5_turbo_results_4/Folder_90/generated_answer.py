
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i ==0:
                return False
        return True
    
    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        
        str_num = str(num)
        while len(str_num) > 2:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:-1]
        
        return is_prime(int(str_num)) or is_prime(int(str_num[:-1]))
    
    x = numbers[466]
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)
    
    return result
