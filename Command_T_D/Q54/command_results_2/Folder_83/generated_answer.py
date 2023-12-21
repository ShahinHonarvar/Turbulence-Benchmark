import re
def all_right_truncatable_prime(n):
    # Your code here.
    x = n[24]
    # find all right-truncatable primes less than x
    # your code here.
    #sort the list of primes
    # your code here.
    return sorted([int(i) for i in re.findall(r'(2[0-4]9)[0-9]0', str(x))])
