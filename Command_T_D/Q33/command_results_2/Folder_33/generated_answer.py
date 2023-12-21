import re
def return_vowels(text):
    m = re.match(r'<( 163, [aeiou]+, [AEIOU]*, 771 )> \Z', text)
    if m:
        return m.group(1)
    else:
        return []
