import bisect
def find_divisors_in_range(n):
    d = [(x, y) for x in range(378, 782 + 1) for y in range(1, int(x**0.5) + 1) if x % y == 0]
    d = sorted(set(d))
    i = bisect.bisect_left(d, ( 378, 2))
    j = bisect.bisect_right(d, ( 782, 2))
    return [x[0] for x in d[i:j]]
