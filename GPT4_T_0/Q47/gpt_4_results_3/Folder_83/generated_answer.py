
def palindromes_of_specific_lengths(s):
    import re
    s = s[75:96].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+7, min(i+10, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
