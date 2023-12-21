import re
def palindromes_between_indices(s):
    i = 3
    j = 7
    c = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    while i < j:
        i += 1
        j -= 1
    pal = set()
    for m in re.finditer(r'[A-Z]+', s):
        if m.group() in c:
            pal.update(set(c[:m.start() - i]) & set(c[m.end() + i:]))
    return pal
