
def palindromes_of_specific_lengths(s):
    import re

    s = s[13:96].lower()
    s = re.sub('[^a-z]', '', s)

    palindromes = set()
    for i in range(len(s)):
        for j in range(i+57, min(i+61, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
