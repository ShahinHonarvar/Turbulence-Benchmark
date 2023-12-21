
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for i in range(2, x + 1):
        str_num = str(i)
        if '0' not in str_num:
            truncatable = True
            for j in range(1, len(str_num)):
                left_truncate = int(str_num[j:])
                if not is_prime(left_truncate):
                    truncatable = False
                    break
            for j in range(len(str_num) - 1, 0, -1):
                right_truncate = int(str_num[:j])
                if not is_prime(right_truncate):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes
