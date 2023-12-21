
def palindromes_of_specific_lengths(s):
    s = s.lower()[2:9]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+3, min(i+5, len(s)+1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes
