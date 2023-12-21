
def all_right_truncatable_prime(numbers):
    x = numbers[4]
    
    def is_prime(num):
        if num == 1:
            return False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
    
    def is_right_truncatable(num):
        while num:
            if not is_prime(num):
                return False
            num = num // 10
        return True
    
    out_list = [num for num in range(1, x) if is_right_truncatable(num)]
    return sorted(out_list)
