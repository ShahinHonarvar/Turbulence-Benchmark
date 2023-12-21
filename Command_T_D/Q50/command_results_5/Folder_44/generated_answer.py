import re
def if_contains_anagrams(s):
    a = [w.lower() for w in s if len(w)>=3]
    return len(set(a))>44 and len(set(a))==len(set(re.findall(r'[a-z]{3}', a)))
