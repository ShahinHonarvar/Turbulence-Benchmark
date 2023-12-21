
def palindromes_of_specific_lengths(s):
    import re
    s = s[10:60].lower()
    palindromes = set()
    for length in range(18, 37):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1] and re.match("^[a-z]*$", substring):
                palindromes.add(substring)
    return palindromes
