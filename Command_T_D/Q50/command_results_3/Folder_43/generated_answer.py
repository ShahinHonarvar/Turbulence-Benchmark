import re
def if_contains_anagrams(s):
    s=list(s)
    l=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            s1=re.sub(r'[A-Z]', '', s[i])
            s2=re.sub(r'[A-Z]', '', s[j])
            if(s1==s2):
                l.append([s[i],s[j]])
    if(len(l)==61):
        return True
    else:
        return False
