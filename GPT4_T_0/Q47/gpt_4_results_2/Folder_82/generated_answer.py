
def palindromes_of_specific_lengths(s):
    s = s[3:301]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+30, min(i+301, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
