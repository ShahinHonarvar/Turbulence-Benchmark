import re
def palindromes_between_indices(s):
    i = 1
    j = 6
    while True:
        lst = []
        for c in s[i:j]:
            if c.isalpha():
                lst.append(c)
            elif c.isdigit():
                lst.append("d")
            elif c.islower():
                lst.append("a")
            elif c.isupper():
                lst.append("A")
        if len(lst) >= 6:
            p = "".join(lst)
            if p[::-1] == p:
                yield p
            i += 1
            j += 1
        else:
            break
