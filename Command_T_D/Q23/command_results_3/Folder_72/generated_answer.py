import re
def find_divisors_in_range(n):
    s = set(re.findall(r'([32-90])', str(n)))
    return [k for k in range(32, n//2 + 1, 2) if n % k == 0 and k in s]
