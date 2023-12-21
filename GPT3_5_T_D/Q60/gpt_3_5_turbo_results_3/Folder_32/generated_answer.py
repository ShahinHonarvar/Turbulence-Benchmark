
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
           return False
        for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
        return True
    
    def is_truncatable_prime(n):
        str_num = str(n)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i+1])):
                return False
        return True
    
    x = numbers[42]
    result = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result)
