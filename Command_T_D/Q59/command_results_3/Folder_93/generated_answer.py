import re
def all_left_truncatable_prime(n):
    for i in range(2, n[11]):
        if left_truncatable_prime_re.match(str(i)):
            yield i
    for i in range(3, int(str(n[11]).lstrip('0'))+1):
        if left_truncatable_prime_re.match(str(i)):
            yield i
