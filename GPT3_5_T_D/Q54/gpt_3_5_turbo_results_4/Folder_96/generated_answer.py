
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    truncatable_primes = []
    
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp >= 10:
                temp = temp // 10
                if not is_prime(temp):
                    break
            else:
                truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
