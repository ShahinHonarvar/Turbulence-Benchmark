import collections
def if_contains_anagrams(s):
    a=[]
    for i in s:
        b=set(i)
        c=[]
        for j in b:
            for k in range(26):
                if chr(j+k) in b:
                    c.append(chr(j+k))
        c=set(c)
        if c in a:
            return False
        a.append(c)
    return True
