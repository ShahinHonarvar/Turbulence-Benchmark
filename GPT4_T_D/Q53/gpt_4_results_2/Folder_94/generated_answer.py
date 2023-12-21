
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'[^a-z]', '', s.lower())
    subset = {s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) >= 41}
    return {ss for ss in subset if ss == ss[::-1]}
