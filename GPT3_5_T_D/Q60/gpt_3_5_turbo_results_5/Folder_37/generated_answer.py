
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    x = numbers[35]
    for number in range(x, 9, -1):
        if '0' in str(number):
            continue
        temp = str(number)
        is_truncatable_prime = True
        while len(temp) > 0 and is_truncatable_prime:
            if not is_prime(int(temp)):
                is_truncatable_prime = False
            temp = temp[:-1]
        if is_truncatable_prime:
            temp = str(number)
            while len(temp) > 0 and is_truncatable_prime:
                if not is_prime(int(temp)):
                    is_truncatable_prime = False
                temp = temp[1:]
        if is_truncatable_prime:
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)
