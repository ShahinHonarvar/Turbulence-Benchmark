
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_right_truncatable_prime(n):
        if n < 10 and str(n)[0] != '1':
            return False
        for i in range(1, int(len(str(n)) / 2) + 1):
            if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[-i:])):
                return False
        return True
    
    prime_numbers = []
    for n in range(2, numbers[3] + 1):
        if is_left_right_truncatable_prime(n):
            prime_numbers.append(n)
    
    return sorted(prime_numbers, reverse=True)
