from functools import reduce
from operator import and_
def find_original_set(s):
    s = [set(s)]
    s = [ reduce(and_, (s[i] for i in range(len(s))))) for j in range(len(s)) ]
    s = [set(i) for i in s]
    return min(s)
