
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                left = True
                for i in range(len(str_num)):
                    if not is_prime(int(str_num[i:])):
                        left = False
                        break
                if left:
                    right = True
                    for i in range(len(str_num), 0, -1):
                        if not is_prime(int(str_num[:i])):
                            right = False
                            break
                    if right:
                        primes.append(num)
    return sorted(primes)
