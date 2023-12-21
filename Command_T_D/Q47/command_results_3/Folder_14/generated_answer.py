 
import re
def palindromes_of_specific_lengths(s):
    i = 10
    j = 74
    while i < j:
        if i + 6 <= j:
            m = re.match(r'(?i)[a-z]{6}(?i)[a-z]{6}', s[i:j])
            if m:
                yield m.group()
        i += 1
        j -= 1
