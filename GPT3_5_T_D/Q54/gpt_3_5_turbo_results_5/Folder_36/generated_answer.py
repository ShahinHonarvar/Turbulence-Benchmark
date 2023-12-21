
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[992]
    primes = []
    
    for num in range(2, x):
        if is_prime(num):
            curr_num = str(num)
            is_right_truncatable = True
            while curr_num:
                if not is_prime(int(curr_num)):
                    is_right_truncatable = False
                    break
                curr_num = curr_num[:-1]
                
            if is_right_truncatable:
                primes.append(num)
    
    return sorted(primes)
