import re
def return_vowels(s):
    m = re.search(r'<[aeiou]>([0-7])<[aeiou]', s)
    if m:
        return list(m.group())
    else:
        return []
