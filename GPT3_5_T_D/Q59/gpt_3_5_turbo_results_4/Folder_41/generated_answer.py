
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    
    truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i):
            curr_num = str(i)
            is_truncatable_prime = True
            while len(curr_num) > 1:
                curr_num = curr_num[1:]
                if not is_prime(int(curr_num)):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(i)
    
    return sorted(truncatable_primes, reverse=True)
