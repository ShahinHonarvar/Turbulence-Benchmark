import re
def palindromes_between_indices(s):
    if not s:
        return set()
    try:
        if not s[0].isalpha():
            return set()
        le, ri = s[0].lower(), s[6].lower()
        return set(re.findall(r'[a-z]+', f'{le}{{6}}{ri}'))
    except:
        return set()
