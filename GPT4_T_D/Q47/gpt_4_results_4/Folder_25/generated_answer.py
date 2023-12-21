
import re
def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    pattern = r"[A-Za-z]"
    pal_set = set()
    for i in range(30, 47):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if re.match(pattern, substring) and substring == substring[::-1]:
                pal_set.add(substring)
    return pal_set
