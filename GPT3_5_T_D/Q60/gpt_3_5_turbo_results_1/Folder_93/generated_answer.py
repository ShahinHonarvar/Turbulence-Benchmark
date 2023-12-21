
def all_left_right_truncatable_prime(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(number):
        str_number = str(number)
        while len(str_number) > 1:
            str_number = str_number[1:]
            if not is_prime(int(str_number)):
                return False
        return True
    
    def is_right_truncatable_prime(number):
        str_number = str(number)
        while len(str_number) > 1:
            str_number = str_number[:-1]
            if not is_prime(int(str_number)):
                return False
        return True
    
    x = numbers[11]
    truncatable_primes = []
    
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
