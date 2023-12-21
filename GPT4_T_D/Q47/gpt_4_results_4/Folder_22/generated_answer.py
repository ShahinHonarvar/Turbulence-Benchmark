
def palindromes_of_specific_lengths(s):
    import re
    s = s.lower()
    subset = s[100:201]
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i+5, min(i+11, len(subset)+1)):
            substring = subset[i:j]
            if substring == substring[::-1] and re.match("^[a-z]*$", substring):
                palindromes.add(substring)
    return palindromes
