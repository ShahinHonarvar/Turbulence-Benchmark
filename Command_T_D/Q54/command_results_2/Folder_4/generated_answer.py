import math
def all_right_truncatable_prime(lst):
    max_x = lst[96]
    lst = [n for n in range(2, max_x // 2 + 1) if all(n % d for d in range(3, int(math.sqrt(n)) + 1, 2))]
    return [n for n in lst if all(str(n).rstrip('0')[::-1].count('9') == 1)]
