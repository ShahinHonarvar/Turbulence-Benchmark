import re
def return_n_smallest_chars(s):
    i=0
    j=len(s)-1
    return [x for x in s if s[i]<=x<=s[j]]
