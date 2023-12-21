
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[18]
    truncate_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = str(num)
            trunc = True
            while len(temp) > 1:
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    trunc = False
                    break
            if trunc:
                truncate_primes.append(num)
    
    return sorted(truncate_primes, reverse=True)
