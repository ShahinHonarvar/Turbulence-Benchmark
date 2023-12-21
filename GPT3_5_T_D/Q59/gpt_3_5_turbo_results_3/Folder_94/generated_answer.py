
def all_left_truncatable_prime(numbers):
    x = numbers[43]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_str = str(num)
            if '0' not in num_str:
                is_truncatable = True
                for j in range(1, len(num_str)):
                    trunc_num = int(num_str[j:])
                    is_truncatable = is_prime_number(trunc_num)
                    if not is_truncatable:
                        break
                if is_truncatable:
                    primes.append(num)
    primes.sort()
    return primes

def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
