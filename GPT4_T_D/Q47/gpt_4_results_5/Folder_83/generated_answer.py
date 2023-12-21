
def palindromes_of_specific_lengths(s):
    import re
    s = s[75:96].lower()
    p_set = set()
    for i in range(len(s)):
        for j in range(i + 7, min(i + 10, len(s) + 1)):
            substring = s[i:j]
            if re.match('[a-z]*$', substring) and substring == substring[::-1]:
                p_set.add(substring)
    return p_set
