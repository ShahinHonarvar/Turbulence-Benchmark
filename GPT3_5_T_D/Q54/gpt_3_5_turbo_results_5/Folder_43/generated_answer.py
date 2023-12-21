
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 89:
        return []
    
    x = numbers[89]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            num = str(i)
            while num != "":
                if not is_prime(int(num)):
                    right_truncatable = False
                    break
                num = num[:-1]
            if right_truncatable:
                right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes, reverse=True)
