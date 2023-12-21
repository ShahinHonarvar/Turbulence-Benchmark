
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for num in range(x):
        if is_prime(num):
            temp = num
            while temp > 9:
                temp = temp // 10
                if not is_prime(temp):
                    break
            else:
                primes.append(num)
    return primes
