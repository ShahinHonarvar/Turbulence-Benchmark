import re
def palindromes_between_indices(s):
    s = re.sub(r'[^A-Za-z]','',s)
    return {x[::-1] for x in (s[i:j] for i in range(2,len(s)-5) for j in range(i+4,len(s)))}
