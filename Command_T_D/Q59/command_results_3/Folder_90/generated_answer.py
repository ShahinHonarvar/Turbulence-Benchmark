import re
import itertools
def all_left_truncatable_prime(nums):
    return sorted(list(filter(left_truncatable_re.match, (n for n in nums if all(n % d == 0 for d in (2, 3, 5, 7))))))
