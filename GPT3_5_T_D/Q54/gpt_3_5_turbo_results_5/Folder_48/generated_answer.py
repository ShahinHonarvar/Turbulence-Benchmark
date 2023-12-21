
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_right_truncatable_prime(num):
        num_str = str(num)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    
    x = numbers[835]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
