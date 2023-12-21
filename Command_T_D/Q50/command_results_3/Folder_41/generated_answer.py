def if_contains_anagrams(s):
    return len(s)>=75 and len(s[0])>=3 and len(s[1])>=3 and len(s)%2==0 and len(s[0])==len(s[1])==len(s[2])==3 and [s[0]]+s+[s[0]]!=s and set(s)!=set(s[0]) and set(s)!=set(s[1]) and set(s)!=set(s[2]) and s[0]!=s[1] and s[0]!=s[2] and s[1]!=s[2]
