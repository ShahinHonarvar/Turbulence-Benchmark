
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[97]
    for num in range(2, x+1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                is_left_truncatable = True
                is_right_truncatable = True
                for i in range(1, len(num_str)):
                    if not is_prime(int(num_str[i:])):
                        is_left_truncatable = False
                        break
                for i in range(len(num_str)-1, 0, -1):
                    if not is_prime(int(num_str[:i])):
                        is_right_truncatable = False
                        break
                if is_left_truncatable and is_right_truncatable:
                    primes.append(num)
    primes.sort(reverse=True)
    return primes
