import re
def palindrome_of_length_n(s):
    for i in range(len(s)):
        if i == len(s) // 2:
            continue
        if s[i:i + 257] == s[i + 256:]:
            yield re_pal.sub(r'\d', '', s[i:i + 257])
