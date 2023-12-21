
def palindromes_of_specific_lengths(s):
    import re
    s = s[11:84]
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(s)):
            substring = s[i:i+length]
            if len(substring) == length:
                clean_substring = re.sub("[^a-z]", "", substring.lower())
                if clean_substring == clean_substring[::-1]:
                    palindromes.add(substring)
    return palindromes
