
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[42]
    primes = []
    for num in range(2, x+1):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                truncatable = True
                for i in range(1, len(str_num)):
                    if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                        truncatable = False
                        break
                if truncatable:
                    primes.append(num)
    return sorted(primes)
