import collections
def if_contains_anagrams(s):
    c=0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i]==s[j]):
                continue
            elif(s[i] in s[j]):
                continue
            elif(s[j] in s[i]):
                continue
            elif(s[i]!=s[j]):
                c+=1
                break
    return c>72
