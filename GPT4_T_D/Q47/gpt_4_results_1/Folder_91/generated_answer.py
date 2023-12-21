
def palindromes_of_specific_lengths(s):
    s = s[0:11].lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 3, min(start + 6, len(s) + 1)):
            substr = s[start:end]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
