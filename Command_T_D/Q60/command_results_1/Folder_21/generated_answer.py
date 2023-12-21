
import sys
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(10**7)

table = {}

for num in range(2, 1_000_000):
    digits = str(num)
    if len(digits) == 1:
        continue
    if digits[0] == '0':
        continue
    if digits[0] in '2357':
        continue
    if digits[-1] == '0':
        continue
    if digits[-1] in '2357':
        continue
    if digits[0] == digits[-1]:
        continue
    if num not in table:
        table[num] = True
        table[num // 10**i] = True
        for i in range(1, len(digits) - 1):
            if digits[i] == '0':
                continue
            if digits[i] not in '2357':
                table[num // 10**(i + 1)] = True
                break
    if digits[0] != digits[-1]:
        table[num // 10**(len(digits) - 1)] = True

def all_left_right_truncatable_prime(nums):
    return sorted(set(table))
