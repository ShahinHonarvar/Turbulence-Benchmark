
def palindromes_of_specific_lengths(s):
    import re
    s = s[101:293].lower()
    s = re.sub('[^a-z]+', '', s)
    length = len(s)
    palindromes = set()
    for i in range(154, min(length, 183)):
        for j in range(0, length - i + 1):
            substring = s[j:j+i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
