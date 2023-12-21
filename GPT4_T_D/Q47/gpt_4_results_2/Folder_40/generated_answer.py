
def palindromes_of_specific_lengths(s):
    s = s[:6]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+3, min(i+6, len(s)+1)):
            substring = s[i:j]
            if (
                substring == substring[::-1] and
                all(c.isalpha() for c in substring)
            ):
                palindromes.add(substring.lower())
    return palindromes
