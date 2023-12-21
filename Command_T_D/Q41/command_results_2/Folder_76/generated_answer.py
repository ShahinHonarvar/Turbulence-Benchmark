import bisect
import setuptools
    d[x] = i
def identical_elements(a, b):
    indices = set(bisect.bisect_left(a, b) + bisect.bisect_left(b, a))
    return set(a[indices[0]:indices[1]])
