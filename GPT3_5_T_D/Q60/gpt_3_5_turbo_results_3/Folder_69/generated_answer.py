
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    truncatable_primes = []

    for num in range(2, x + 1):
        prime = True
        str_num = str(num)
        if '0' in str_num:
            prime = False
        else:
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:i])) or not is_prime(int(str_num[i:])):
                    prime = False
                    break
        if prime:
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
