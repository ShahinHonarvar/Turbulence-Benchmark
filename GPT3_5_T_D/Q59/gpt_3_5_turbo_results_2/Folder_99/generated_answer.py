
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[758]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            remove_digit = 1
            while remove_digit < len(num):
                truncated_num = int(num[remove_digit:])
                if not is_prime(truncated_num):
                    break
                remove_digit += 1
            else:
                left_truncatable_primes.append(i)
    
    return left_truncatable_primes
