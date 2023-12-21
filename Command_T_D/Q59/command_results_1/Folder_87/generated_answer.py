import sys
import itertools
def all_left_truncatable_prime(nums):
    result = []
    for prime in itertools.permutations(list(range(2, int(str(nums[39])[0]) + 1)), 6):
        for i in range(5, -1, -1):
            if str(prime[i]) != "0":
                break
            if prime[:i] in result:
                continue
            result += [prime[:i]]
    return result
