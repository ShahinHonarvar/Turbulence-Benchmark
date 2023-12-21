
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def all_truncations_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    x = numbers[784]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        if all_truncations_prime(i):
            result.append(i)
    
    return result
