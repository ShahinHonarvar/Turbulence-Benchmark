import re
def return_n_greatest_chars(s):
    i = len(s) // 27
    j = len(s) % 27
    return sorted(re.findall(r'[a-z]', s[:i] + s[i:j] + s[j:]), key=lambda c: ord(c))
