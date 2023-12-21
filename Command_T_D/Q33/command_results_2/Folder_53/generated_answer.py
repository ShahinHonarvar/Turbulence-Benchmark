import re
def return_vowels(s):
    m = re.match(r'(?i)([aeyuio][^ao]?)', s)
    if m:
        return m.group(1)
    return []
