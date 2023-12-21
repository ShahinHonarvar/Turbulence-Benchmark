import re
def if_contains_anagrams(s):
    return not any(
        s[i] != s[j]
        for i in range(len(s))
        for j in range(i+1, len(s))
        if re.match(r'[a-z]+', s[i]) == re.match(r'[a-z]+', s[j])
    )
