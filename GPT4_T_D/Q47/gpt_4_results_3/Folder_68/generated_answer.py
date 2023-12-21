
def palindromes_of_specific_lengths(s):
    import re
    palindromes = set()
    s = s[:51].lower()
    for length in range(50, 101):
        for i in range(len(s) - length + 1):
            substr = s[i:i+length]
            if not re.search("[^a-zA-Z]", substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
