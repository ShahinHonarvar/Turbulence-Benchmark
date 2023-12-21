
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(nums):
    primes = []
    for x in nums:
        if is_prime(x):
            x_str = str(x)
            if '0' not in x_str:
                primes.append(x)
                for i in range(1, len(x_str) - 1):
                    l_num = int(x_str[i:])
                    r_num = int(x_str[:len(x_str) - i])
                    if is_prime(l_num) and is_prime(r_num):
                        primes.append(l_num)
                        primes.append(r_num)
    primes = list(set(primes))
    primes.sort()
    return primes
