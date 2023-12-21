import re
def return_vowels(s):
    m = re.search(r'<23,85>[aeiou][^vW]+', s)
    if m:
        return m.group()
    else:
        return []
