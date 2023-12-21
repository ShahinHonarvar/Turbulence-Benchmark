import re
def if_contains_anagrams(s):
    cnt=0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i] == s[j]):
                continue
            elif(re.fullmatch(s[i],s[j]) is not None):
                cnt += 1
    return cnt>=72
