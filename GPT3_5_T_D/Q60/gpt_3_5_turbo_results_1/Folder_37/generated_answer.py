
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if str_num[i] == '0':
                return False
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                return False
            truncated_num = int(str_num[:i])
            if not is_prime(truncated_num):
                return False
        return True
    
    x = numbers[35]
    result = []

    for num in range(x, 0, -1):
        if is_truncatable_prime(num):
            result.append(num)
    
    return result
