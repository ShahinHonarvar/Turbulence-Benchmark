
def palindromes_of_specific_lengths(s):
    s = s[125:284]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 109, min(start + 127, len(s) + 1)):
            substr = s[start:end]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr)
    return palindromes
