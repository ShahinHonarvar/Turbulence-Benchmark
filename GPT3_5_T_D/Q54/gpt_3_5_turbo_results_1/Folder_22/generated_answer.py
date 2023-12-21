
def all_right_truncatable_prime(numbers):
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    x = numbers[85]
    truncatable_primes = []
    for num in range(2, x):
        temp_num = num
        is_truncatable = True
        while temp_num > 0:
            if not is_prime(temp_num):
                is_truncatable = False
                break
            temp_num //= 10
        if is_truncatable:
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
