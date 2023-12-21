
def palindromes_of_specific_lengths(s):
    import re
    s = s[16:95].lower()
    s = re.findall(r'\b\w+\b', s)
    l = []
    for word in s:
        if 39 <= len(word) <= 52 and word == word[::-1]:
            l.append(word)
    return set(l)
