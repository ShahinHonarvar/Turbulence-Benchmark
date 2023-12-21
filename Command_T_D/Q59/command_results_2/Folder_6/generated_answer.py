import itertools
def all_left_truncatable_prime(nums):
    return sorted(list(set(itertools.chain.from_iterable(
        num for num in nums if is_left_truncatable_prime(num)
    )))))
def is_left_truncatable_prime(num):
    if not num or num == '0':
        return False
    if num == '1':
        return True
    s = str(num)
    while s[0] in '0123456789':
        s = s[1:]
    return all(n for n in range(2, int(s, 10) + 1) if all(n % r == 0 for r in range(3, int(s, 10) + 1, 2)))
