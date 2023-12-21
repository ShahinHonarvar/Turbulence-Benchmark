import re
def if_contains_anagrams(s):
    return sum(1 for i in range(len(s)) for j in range(i+1,len(s)) if (re.match(r'[a-z]{3}(?=\s[a-z]{3})', s[i].lower()) and re.match(r'[a-z]{3}(?=\s[a-z]{3})', s[j].lower())) <= 48)
