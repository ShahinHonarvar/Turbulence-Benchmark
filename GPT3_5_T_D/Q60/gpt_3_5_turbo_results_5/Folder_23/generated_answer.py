
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]

    def is_truncatable_prime(number):
        if '0' in str(number):
            return False
        
        while len(str(number)) > 2:
            if not is_prime(number):
                return False
            number = int(str(number)[1:-1])
        
        return is_prime(number)
    
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)

    return result
