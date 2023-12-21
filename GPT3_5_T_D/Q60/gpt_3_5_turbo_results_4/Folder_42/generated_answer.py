
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    truncatable_primes = []
    
    for num in range(2, x+1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                is_truncatable = True
                for i in range(len(num_str)-1):
                    trunc_left = int(num_str[i+1:])
                    trunc_right = int(num_str[:len(num_str)-i-1])
                    if not (is_prime(trunc_left) and is_prime(trunc_right)):
                        is_truncatable = False
                        break
                if is_truncatable:
                    truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
