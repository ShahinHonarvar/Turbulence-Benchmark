
import itertools
import re

def all_left_right_truncatable_prime(nums):
    x = nums[50]
    res = []
    for n in range(2, x+1):
        # Find all primes
        primes = set(n for n in range(2, n+1) if all(n % d for d in range(3, int(n ** .5) + 1, 2)))
        # Find all left-and-right-truncatable primes
        ll = [str(p) for p in primes if p > 9 and len(str(p)) > 2]
        rr = [str(p) for p in primes if p > 9 and len(str(p)) > 1]
        lrr = [p for p in range(10, min(ll) + 1) if p not in ll]
        rll = [p for p in range(10, min(rr) + 1) if p not in rr]
        # Generate all left-and-right-truncatable primes
        all_ll = itertools.permutations(ll + lrr)
        all_rr = itertools.permutations(rr + rll)
        # Filter out non-left-and-right-truncatable primes
        for ll, rr in all_ll + all_rr:
            if (ll[-1] == '0' or ll[0] == '0' or ll[1] == '0') and ll[0] != '1':
                continue
            if (rr[-1] == '0' or rr[0] == '0' or rr[1] == '0') and rr[0] != '1':
                continue
            # Test if the number remains prime
            if all(n % d == 0 for d in range(3, int(ll[0] ** .5) + 1, 2)):
                continue
            if all(n % d == 0 for d in range(3, int(rr[0] ** .5) + 1, 2)):
                continue
            # Add to the list of primes
            res.append(int(ll[0] + rr[0]))
    return res
