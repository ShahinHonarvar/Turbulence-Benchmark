import re
def return_vowels(s):
    m = re.match(r'[aieouAEIOU]([jJ]?)', s)
    return m.group(1)
