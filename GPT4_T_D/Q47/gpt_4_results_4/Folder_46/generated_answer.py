
def palindromes_of_specific_lengths(s):
    import re
    s = s[11:98]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start, len(s)):
            substring = s[start:end+1]
            if len(substring) >= 29 and len(substring) <= 62 and re.match("^[A-Za-z]*$", substring):
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes
