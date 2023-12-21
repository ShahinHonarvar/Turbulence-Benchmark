 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[87]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            temp_num = str(num)
            while temp_num:
                if not is_prime(int(temp_num)):
                    truncatable = False
                    break
                temp_num = temp_num[1:]
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
