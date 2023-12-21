import re
def return_vowels(s):
    if not s:
        return []
    else:
        m = re.fullmatch(r'<[aeiou][^>]*z', s)
        if m:
            return s[m.start():m.end()]
        else:
            return []
