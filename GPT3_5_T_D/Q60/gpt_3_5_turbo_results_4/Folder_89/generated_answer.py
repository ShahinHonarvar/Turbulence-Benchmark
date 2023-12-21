
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    truncatable_primes = []
    
    for n in range(2, x + 1):
        if all(int(digit) != 0 for digit in str(n)) and is_prime(n):
            is_truncatable = True
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(n)
    
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
