import sys
def find_original_set(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10):
    x = set(s1).union(s2)
    x = x.union(s3)
    x = x.union(s4)
    x = x.union(s5)
    x = x.union(s6)
    x = x.union(s7)
    x = x.union(s8)
    x = x.union(s9)
    x = x.union(s10)
    return x
