
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[88]
    
    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        else:
            n_str = str(n)
            if not is_prime(n):
                return False
            for i in range(1, len(n_str)):
                if not is_prime(int(n_str[:-i])) or not is_prime(int(n_str[i:])):
                    return False
            return True
    
    for num in range(x, 0, -1):
        if is_truncatable_prime(num):
            result.append(num)
    
    return result
