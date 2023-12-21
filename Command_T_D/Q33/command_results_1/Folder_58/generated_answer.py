import re
def return_vowels(s):
    m = re.search(r'[^aieou]{%: 260}([aieou])[%:%: 322]', s)
    return m.group(1) if m else []
