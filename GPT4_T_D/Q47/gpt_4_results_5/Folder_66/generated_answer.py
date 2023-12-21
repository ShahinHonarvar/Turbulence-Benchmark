
def palindromes_of_specific_lengths(s):
    import re
    s = s[32:80]
    all_palindromes = set()
    for i in range(len(s)):
        for j in range(i+35, min(i+42, len(s)+1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and re.match("^[A-Za-z]*$", substring):
                all_palindromes.add(substring)
    return all_palindromes
