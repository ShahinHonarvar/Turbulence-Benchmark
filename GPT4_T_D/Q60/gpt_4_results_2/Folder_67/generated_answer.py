
from itertools import permutations

def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def check_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n:
                return False
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    trunc_primes = []
    x = nums[71]

    for length in range(1, len(str(x)) + 1):
        for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], length):
            num = int(''.join(map(str, perm)))
            if num <= x and is_prime(num) and check_truncatable(num):
                trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)
