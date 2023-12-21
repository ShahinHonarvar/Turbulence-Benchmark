
def palindromes_of_specific_lengths(s):
    import re
    palindromes = set()
    s = s[41:90]
    for length in range(23, 39):
        for i in range(len(s)-length+1):
            substr = s[i:i+length]
            if re.match(r"^[A-Za-z]*$", substr) and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes
