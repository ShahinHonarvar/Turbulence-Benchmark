import itertools
def all_left_truncatable_prime(nums):
    left_truncatable_primes = []
    for n in range(2, nums[86] + 1):
        for i in range(1, int(str(n)) + 1):
            if n % 10 ** i == 0:
                break
            elif str(n)[:i] in ("0", "5"):
                continue
            elif str(n)[i:] in ("5", "6", "7", "8", "9"):
                break
            elif n == int(str(n)[:i]):
                continue
            elif n == int(str(n)[i:]):
                continue
            elif str(n)[i:] == str(n):
                continue
            elif str(n)[i:] == str(n)[:-1]:
                break
            else:
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)
