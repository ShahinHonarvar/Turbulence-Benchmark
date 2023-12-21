
def all_left_right_truncatable_prime(numbers):
    primes = []
    for i in range(len(numbers)):
        num = numbers[i]
        if is_left_and_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_left_and_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(len(str(num))-1):
        if str(num)[i] == '0':
            return False
        if not is_prime(int(str(num)[:i+1]) and int(str(num)[i+1:])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
