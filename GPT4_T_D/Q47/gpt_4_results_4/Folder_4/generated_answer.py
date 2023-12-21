
import re
def palindromes_of_specific_lengths(s):
    s = s[12:93]
    s = re.sub('[^a-z]', '', s.lower())
    res = set()
    for i in range(17, 67):
        for j in range(len(s)-i+1):
            sub = s[j:j+i]
            if sub == sub[::-1]:
                res.add(sub)
    return res
