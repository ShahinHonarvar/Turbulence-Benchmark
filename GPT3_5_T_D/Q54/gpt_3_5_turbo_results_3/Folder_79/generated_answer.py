
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[91]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = str(num)
            is_right_truncatable_prime = True
            while len(temp) > 1:
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
