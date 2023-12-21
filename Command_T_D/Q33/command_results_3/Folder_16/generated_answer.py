import re
def return_vowels(s):
    m = re.match(r'<(\d+)-(\d+)>(\w)+', s)
    if m:
        start, stop, c = int(m.group(1)), int(m.group(2)), m.group(3)
        return [i for i in range(start, stop) if chr(i) in c]
    else:
        return []
