
def palindromes_of_specific_lengths(s):
    import re
    s = s[29:99]
    s = re.sub('[^a-zA-Z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, min(i + 10, len(s) + 1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
