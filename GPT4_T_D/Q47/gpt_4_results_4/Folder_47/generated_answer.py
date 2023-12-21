
def palindromes_of_specific_lengths(s):
    s = s[39:95]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+14, min(i+53, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
