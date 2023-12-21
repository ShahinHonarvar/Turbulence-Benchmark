
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[36]
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        left_truncatable = True
        right_truncatable = True
        temp = num
        while temp > 10:
            temp //= 10
            if not is_prime(temp):
                left_truncatable = False
                break
        temp = num % (10 ** (len(str(num))-1))
        while temp >= 10:
            if not is_prime(temp):
                right_truncatable = False
                break
            temp = temp % (10 ** (len(str(temp))-1))
        if left_truncatable and right_truncatable:
            primes.append(num)
    return sorted(primes)
