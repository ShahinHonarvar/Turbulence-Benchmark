
def palindromes_of_specific_lengths(s):
    s = s[29:99]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+6, min(i+10, len(s)+1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes
