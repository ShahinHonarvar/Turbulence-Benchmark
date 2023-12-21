
def palindromes_of_specific_lengths(s):
    s = s[11:88]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+4, min(i+6, len(s)+1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j].lower())
    return palindromes
