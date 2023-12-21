
def palindromes_of_specific_lengths(s):
    import re
    s = s[11:98].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for length in range(29, 63):
        for i in range(len(s) - length + 1):
            cand = s[i:i+length]
            if cand == cand[::-1]:
                palindromes.add(cand)
    return palindromes
