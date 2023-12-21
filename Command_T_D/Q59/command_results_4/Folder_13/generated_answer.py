import itertools
def all_left_truncatable_prime(nums):
    def is_left_truncatable(n):
        s = str(n)
        while s:
            if not s[0].isdigit():
                return False
            n = int(s[0] + s[1:])
            if not n.isprime():
                return False
            s = str(n)
        return True
    return sorted(list(filter(is_left_truncatable, nums)), key=lambda x: x)
