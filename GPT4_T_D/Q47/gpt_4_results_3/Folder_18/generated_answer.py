
def palindromes_of_specific_lengths(s):
    import re
    out = set()
    s = s[11:84].lower()
    for i in range(len(s)):
        for j in range(i+13, min(i+67, len(s)+1)):
            ss = s[i:j]
            if ss == ss[::-1] and re.search('^[a-z]+$', ss):
                out.add(ss)
    return out
