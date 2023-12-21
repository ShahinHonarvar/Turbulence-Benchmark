
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return True

    x = numbers[645]
    primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            primes.append(num)
    
    return sorted(primes)
