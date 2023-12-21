
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[7]
    left_truncatable_primes = []

    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:]
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
            if is_truncatable:
                left_truncatable_primes.append(num)

    return sorted(left_truncatable_primes)
