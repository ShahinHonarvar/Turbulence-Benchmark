import re
def return_vowels(s):
    m = re.findall(r'[aeyuio]', s[24:-1])
    return [char for char in m if char.isupper() and char > 'f' and char <= '|']
