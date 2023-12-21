
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def truncate(num):
    num_str = str(num)
    trunc_nums = []
    for i in range(1, len(num_str)):
        trunc_nums.append(int(num_str[i:]))
        trunc_nums.append(int(num_str[:-i]))
    return trunc_nums


def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num) and '0' not in str(num):
            trunc_nums = truncate(num)
            trunc_primes = [n for n in trunc_nums if is_prime(n)]
            if all(is_prime(n) for n in trunc_primes):
                primes.append(num)
    primes.sort(reverse=True)
    return primes
