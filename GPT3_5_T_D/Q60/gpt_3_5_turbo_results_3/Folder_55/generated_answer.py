
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncate(n):
    return int(str(n)[1:])

def right_truncate(n):
    return int(str(n)[:-1])

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    primes = []
    
    for num in range(2, x+1):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 10:
                truncated_num = left_truncate(truncated_num)
                if not is_prime(truncated_num):
                    break
            if truncated_num <= 10:
                primes.append(num)
    
    return sorted(primes, reverse=True)
