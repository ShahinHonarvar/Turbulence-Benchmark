
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    def is_truncatable_prime(n):
        digits = str(n)
        for i in range(len(digits)):
            left = int(digits[i:])
            right = int(digits[:i+1])
            if left < 10 and not is_prime(left):
                return False
            if right < 10 and not is_prime(right):
                return False
        return True

    x = numbers[100]

    primes = []
    for num in range(2, x+1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)

    return primes
