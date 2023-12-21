import re
def all_substring_of_size_n(s):
    lst = []
    for i in range(1, len(s)+1):
        for j in range(i, len(s)+1):
            if s[i-1] == s[j-1]: continue
            lst += [[s[i:j]]
    return lst
