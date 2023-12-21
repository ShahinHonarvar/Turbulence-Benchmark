import re
def all_left_truncatable_prime(nums):
    primes = []
    for n in range(2,int(str(nums[0]))+1):
        s = str(n)
        while s:
            if all(int(s[i]) not in '0123456789' for i in range(1,len(s))):
                break
            s = s[1:]
        if s == '':
            primes.append(n)
    return primes
