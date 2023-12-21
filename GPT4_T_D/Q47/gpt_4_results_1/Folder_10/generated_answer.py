
def palindromes_of_specific_lengths(s):
    import re
    s = s[16:61]
    s = re.sub("[^a-zA-Z]", "", s).lower()
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(s) - length + 1):
            substring = s[i: i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
