
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if num < 10:
            continue
        elif num < 100:
            if is_prime(num):
                primes.append(num)
        else:
            num_str = str(num)
            if '0' in num_str:
                continue
            flag = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i+1])):
                    flag = False
                    break
            if flag:
                primes.append(num)
    return sorted(primes)
