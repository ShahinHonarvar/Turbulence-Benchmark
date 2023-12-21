
def palindromes_of_specific_lengths(s):
    import re
    s = s[30:85]
    palindromes = set()
    for length in range(12, 21):
        for i in range(len(s)-length+1):
            substring = s[i:i+length]
            if substring.lower() == substring[::-1].lower() and \
               re.match("^[a-zA-Z]*$", substring):
                palindromes.add(substring)
    return palindromes
