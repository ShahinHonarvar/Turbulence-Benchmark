
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            is_truncatable_prime = True
            str_num = str(num)
            for i in range(len(str_num)):
                if str_num[i] == '0':
                    is_truncatable_prime = False
                    break
                if not is_prime(int(str_num[i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                primes.append(num)
    return sorted(primes)
