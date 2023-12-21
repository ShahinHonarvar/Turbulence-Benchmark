
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(n):
        str_n = str(n)
        while str_n != '':
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    
    x = numbers[33]
    result = []
    for number in range(2, x):
        if is_prime(number) and is_left_truncatable_prime(number):
            result.append(number)
    
    return sorted(result)
