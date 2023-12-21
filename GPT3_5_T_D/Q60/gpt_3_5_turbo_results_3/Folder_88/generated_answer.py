
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        while len(str(num)) > 2:
            if not is_prime(num):
                return False
            num = int(str(num)[1:-1])
        return is_prime(num)
    
    x = numbers[93]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    
    return sorted(result)
