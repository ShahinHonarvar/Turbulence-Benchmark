
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    primes = []

    for num in range(x-1, 9, -1):
        if is_prime(num):
            temp = str(num)
            is_right_truncatable = True
            while temp != '':
                if not is_prime(int(temp)):
                    is_right_truncatable = False
                    break
                temp = temp[:-1]
            if is_right_truncatable:
                primes.append(num)

    return sorted(primes, reverse=True)
