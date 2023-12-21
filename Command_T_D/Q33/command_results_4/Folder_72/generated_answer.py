import re
def return_vowels(s):
    res = re.findall(r'<[aeiou][^>]*>([a-z]*?)<', s)
    return ['<{}>'.format(e) for e in res if e]
