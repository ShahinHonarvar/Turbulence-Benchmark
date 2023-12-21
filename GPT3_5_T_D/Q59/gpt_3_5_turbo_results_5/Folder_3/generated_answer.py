
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in numbers:
        if num >= 10:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                truncatable = True
                digits = list(str(num))
                while truncatable and digits:
                    if digits[0] == '0':
                        truncatable = False
                    else:
                        num = int(''.join(digits))
                        if not is_prime(num):
                            truncatable = False
                    digits.pop(0)
                if truncatable:
                    primes.append(num)
    primes.sort()
    return primes
