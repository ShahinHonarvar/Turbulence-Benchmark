import re
def return_vowels(string):
    m = re.search(r'<[aeyuio]+>([aeyuio]+)<', string)
    return list(m.group(1))
