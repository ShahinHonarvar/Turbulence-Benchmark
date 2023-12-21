import re
def return_vowels(s):
    res = re.findall(r'<([aeiou])>([5-6])<', s)
    return [x[0] for x in res]
