import re
def return_vowels(s):
    m = re.match(r'[aieou][^;]*[aieou]', s[12:-1])
    if m:
        return list(m.group())
    else:
        return []
