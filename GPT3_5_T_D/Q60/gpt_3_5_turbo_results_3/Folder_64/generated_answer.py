
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[4]
    left_right_truncatable_primes = []
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        truncatable = True
        temp = str(num)
        while len(temp) > 2:
            if not is_prime(int(temp)):
                truncatable = False
                break
            temp = temp[1:-1]
        if truncatable and is_prime(int(temp)):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)
