 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[61]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            temp = str(num)
            while truncatable and temp != "":
                if not is_prime(int(temp)):
                    truncatable = False
                temp = temp[:-1]
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
