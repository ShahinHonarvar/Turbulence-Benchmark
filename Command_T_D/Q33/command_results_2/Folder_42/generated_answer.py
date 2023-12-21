import re
def return_vowels(s):
    m = re.match(r'[A-Z][^;]{%d[^|]{%d}}[A-Z]{%d[^|]{%d}}'
                    % (12, 25, 12, 25), s)
    if m:
        return m.group()
    else:
        return []
