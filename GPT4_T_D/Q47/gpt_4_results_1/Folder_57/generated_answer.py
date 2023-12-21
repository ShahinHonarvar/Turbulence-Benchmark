
def palindromes_of_specific_lengths(s):
    s = s[16:95]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+39, min(i+53, len(s)+1)):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
