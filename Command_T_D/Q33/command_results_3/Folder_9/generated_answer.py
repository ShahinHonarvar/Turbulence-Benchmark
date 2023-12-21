import re
def return_vowels(s):
    m = re.match(r'(?<=.)(A[BL]?)', s)
    if m:
        return m.group(1).upper()
    else:
        return []
