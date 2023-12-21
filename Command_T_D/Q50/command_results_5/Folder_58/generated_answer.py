def if_contains_anagrams(s):
    s=set(s)
    n=len(s)
    s=s.copy()
    s.sort()
    for i in range(n//2):
        for j in range(i+1,n//2):
            s[i].sort()
            s[j].sort()
            if s[i]==s[j]:
                continue
            elif s[i][:len(s[i])//2]==s[j][:len(s[j])//2]:
                continue
            else:
                return True
    return False
