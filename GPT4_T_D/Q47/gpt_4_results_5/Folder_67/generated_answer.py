
def palindromes_of_specific_lengths(s):
    import re
    s = s[65:100]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+26, min(i+34, len(s)+1)):
            substring = s[i:j]
            if re.match("^[A-Za-z]*$", substring):
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes
