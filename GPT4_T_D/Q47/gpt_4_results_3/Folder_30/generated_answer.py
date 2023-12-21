
def palindromes_of_specific_lengths(s):
    s = s[14:91]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+55,i+72):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j].lower())
    return palindromes
